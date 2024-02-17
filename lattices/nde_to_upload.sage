# This script takes input files from Noam Elkies' GP scripts and creates upload files for lat_lattices and lat_genera

magma.attach("canonical_form.m")
from collections import defaultdict
from sage.databases.cremona import class_to_int, cremona_letter_code
opj = os.path.join

def parse_line(line):
    invs, gram = line.strip().split("][")
    res = {}
    res["gram"] = sage_eval("[" + gram.replace(";", ","))
    res["root_string"], res["mw_rank"], res["mw_torsion"], res["root_discriminant"], res["num_reducible_fibers"], res["theta_series"], res["quest"] = sage_eval(invs + "]")
    res["root_lattice"] = parse_root_string(res["root_string"])
    return res

def parse_root_string(s):
    pieces = []
    for part in s.split():
        if "^" not in part:
            n = 1
        else:
            part, n = part.split("^")
            n = ZZ(n)
        for i in range(n):
            pieces.append((part[0], ZZ(part[1:])))
    pieces.sort(reverse=True)
    return tuple(pieces)

def process_genus(genus_label):
    infile = opj("data", "nde_out", genus_label)
    ZZx = ZZ['x']
    with open(infile) as F:
        chunks = F.read().strip().split("\n\n")
        assert len(chunks) == 5
        lats = [parse_line(line) for line in chunks[0].split("\n")]
        genus_data = {}
        n = genus_data["class_number"] = len(lats)
        assert n-1 == chunks[1].count("\n") == chunks[2].count(";") == chunks[3].count("\n")
        for res, aut in zip(lats, chunks[1].split("\n")):
            res["aut_size"] = ZZ(aut)
        genus_data["adjacency_matrix"] = {"2": sage_eval(chunks[2].replace(";", ","))}
        polys = chunks[3].split("\n")
        assert all(f[0] == "[" and f[-1] == "]" for f in polys)
        polys = [f[1:-1].rsplit(" ", 1) for f in polys]
        polys = [[list(ZZx(f[0])), ZZ(f[1])] for f in polys]
        genus_data["adjacency_polynomials"] = {"2": polys}
        mass = chunks[4].lstrip("mass = ")
        if "/" in mass:
            mass = [ZZ(c) for c in mass.split("/")]
        else:
            mass = [ZZ(mass), 1]
        genus_data["mass"] = mass

    def sort_key(res):
        return (res["root_lattice"], prod(res["mw_torsion"]), tuple(res["mw_torsion"]), tuple(res["theta_series"]), res["quest"])

    by_skey = defaultdict(list)
    for lat in lats:
        by_skey[sort_key(lat)].append(lat)
    slats = []
    for key in sorted(by_skey, reverse=True):
        L = by_skey[key]
        if len(L) > 1:
            print("Computing canonical forms", key)
            for lat in L:
                M = magma.MatrixAlgebra(ZZ, ZZ(len(lat["gram"])).isqrt())
                A = M(lat["gram"])
                can = A.CanonicalForm()
                lat["canonical"] = [ZZ(can[i][j]) for i in range(1,ZZ(can.Nrows())+1) for j in range(1,ZZ(can.Ncols())+1)]
            L.sort(key=lambda lat: lat["canonical"], reverse=True)
        slats.extend(L)

    for i, lat in enumerate(slats):
        lat["label"] = f"{genus_label}.{i+1}"

    return genus_data, slats

def rewrite_schema(table):
    fname = table + ".md"
    oname = table + "2.md"
    with open(fname) as F:
        with open(oname, "w") as Fout:
            for line in F:
                if line.count("|") == 3:
                    line = line.strip() + " |"
                if line.count("|") == 4:
                    line = line.strip()
                    pieces = line.split("|")
                    pieces = [piece.strip() for piece in pieces]
                    pieces[2:] = [pieces[3], pieces[2], pieces[4]]
                    line = " | ".join(pieces).strip() + "\n"
                _ = Fout.write(line)

def write_upload_files(genus_label):
    genus_data, lats = process_genus(genus_label)

    # From this data, we need to produce
    # 1 positive-definite entry in the lat_genera table, and 1 for the direct sum with the hyperbolic plane
    # class_number entries in the lat_lattices table for the positive definite latties, and 1 for the indefinite
    # 1 entry in the k3_families table
    # class_number entries in the k3_elliptic table
    # class_number entries in the k3_family_models table (the Weierstrass models of the elliptic surfaces)
    
