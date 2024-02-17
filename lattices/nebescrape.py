from html.parser import HTMLParser
import urllib.request
import urllib.parse
import time
from collections import defaultdict
opj = os.path.join

# Properties: perfect, strongly perfect, eutactic, semi-eutactic, unimodular, N-modular

# bacher.html defines The Bacher polynomials associated with a lattice L:
# With each vector v in L of minimal norm m we associate a univariate polynomial B_v in Z[X] in the following way. Let M_v be the set of minimal vectors in L that have scalar product m/2 with v. For each w in M_v let n_w be the number of pairs (x,y) in M_v x M_v such that all scalar products b(w,x)=b(w,y)=b(x,y)=m/2. Then B_v := sum _{w in M_v} X^n_w.
# The Bacher polynomials are a very strong invariant of the lattice and provide a powerful method for distinguishing between lattices. They often separate the orbits of the automorphism group on the set of minimal vectors of L.

# Minkowski reduced basis for rank up to 4 (nice gram matrices)

# Families: unimodular, the hyperbolic lattice
# Isomorphic combinations of ADE

class LinkExtractor(HTMLParser):
    def __init__(self, *args, **kwds):
        self.links = set()
        HTMLParser.__init__(self, *args, **kwds)

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            D = dict(attrs)
            if "href" in D:
                self.links.add(D["href"])

class SectionExtractor(HTMLParser):
    def __init__(self, *args, **kwds):
        self.cur_section = None
        self.data = defaultdict(list)
        HTMLParser.__init__(self, *args, **kwds)

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            D = dict(attrs)
            if "name" in D:
                if D["name"].lower().startswith("last"):
                    self.cur_section = None
                else:
                    self.cur_section = D["name"]

    def handle_data(self, data):
        if self.cur_section is not None:
            data = data.strip()
            if data and data != self.cur_section:
                self.data[self.cur_section.lower()].append(data)

def follow_links_recursive(base="http://www.math.rwth-aachen.de/~Gabriele.Nebe/LATTICES/", page="index.html", folder="/Users/roed/Downloads/Nebescrape/", seen=None):
    """
    This function downloads all pages from Nebe-Sloane's site.
    """
    url = f"{base}/{page}"
    if seen is None:
        seen = set()
    print("Scraping", page)
    try:
        fname = opj(folder, page)
        if os.path.exists(fname):
            with open(fname) as F:
                contents = F.read()
        else:
            time.sleep(0.5)
            remote = urllib.request.urlopen(url)
            contents = remote.read().decode("ascii")
            with open(opj(folder, page), "w") as F:
                _ = F.write(contents)
        parser = LinkExtractor()
        parser.feed(contents)
        borked = []
        for link in parser.links:
            if link.startswith("ExtLatDat/"):
                trunc = link[10:]
                seen.add(trunc)
                borked.extend(extract_links_recursive(base+"ExtLatDat/", trunc, folder, seen))
            elif ("/" not in link and
                "#" not in link and
                ":" not in link and
                not link.endswith(".gz") and
                link not in seen):
                seen.add(link)
                borked.extend(extract_links_recursive(base, link, folder, seen))
        return borked
    except Exception:
        return [page]

def links(page, folder="/Users/roed/Downloads/Nebescrape/"):
    fname = opj(folder, page)
    if os.path.exists(fname):
        with open(fname) as F:
            contents = F.read()
    parser = LinkExtractor()
    parser.feed(contents)
    return sorted(parser.links)

def Borch25(fname):
    # Describes process for generating all 665 unimodular lattices of dimension 25 (which are in bijection with some other sets of lattices)
    raise NotImplementedError

def Even25(fname):
    # the 121 even 25-dimensional lattices of determinant 2
    raise NotImplementedError

def perfect8(fname):
    # perfect forms in dimension 8; whether eutactic or semi-eutactic; neighbor info
    # Easy to extract Gram matrices; also includes aut size, det??, arith minimum, kissing number, center density
    # Make sure to mark perfect as True
    raise NotImplementedError

def Brandt2(fname):
    # primitive positive-definite ternary quadratic forms of discriminants up to -1000
    # even case
    raise NotImplementedError

def Brandt1(fname):
    # primitive positive-definite ternary quadratic forms of discriminants up to -1000
    # odd case
    raise NotImplementedError

def Nipp4(fname):
    # reduced regular primitive positive-definite quaternary quadratic forms through disc 1732
    # Format in nipp.html
    # Genus info in app1080.html and app1732.html
    # NOTE: For the corrected information compiled by Chul-hee Lee see github tables at https://github.com/chlee-0/nipp; these only affect p-adic densities and p-adic Jordan splittings, not the forms themselves
    raise NotImplementedError

def Nipp5(fname):
    # reduced regular primitive positive-definite quinary quadratic forms through disc 513
    # Format in nipp5.html
    raise NotImplementedError

def Jagy(fname):
    # positive ternary quadratic forms that are spinor regular but are NOT regular, conjectured complete (checked to 575000)
    raise NotImplementedError

def ExtLat(fname):
    # Extremal strongly modular lattices
    # Format in ExtLat.html
    raise NotImplementedError

def noop(fname):
    # Index pages that only have links to other pages and no lattice data themselves
    return []

def magmabasis_to_gram(fname):
    # Need to construct the lattice in Magma from a basis and the get the Gram matrix out via GramMatrix(L42) then rescale;
    raise NotImplementedError

def basis_to_gram(fname):
    # Given the basis in a maybespace-separated format and need to construct Gram matrix, rescale (see HZ40 and GH39 for no spaces)
    raise NotImplementedError

def singleton(fname):
    # Standard format for a single lattice.  We mostly care about the gram section, but it would be worth double checking data in Nebe-Sloane

    # auto
    # bacher_polynomials
    # bacher_polynomials_dual
    # base/basis (comments about rescaling, in magma)
    # comments
    # density/dens/covering_density
    # det/determinant
    # dim/dimension (tabs and required)
    # divisors (elementary divisors)
    # eigenvalues
    # genus
    # glue_vectors
    # gram (in magma; floating point or integer; maple/pari with no space; gram_maple, gram_matrix in maple)
    # group generators/group_generators
    # group order/group_order
    # group_name
    # hermite_number
    # hermitian_group_generators
    # hermitian_group_name
    # hermitian_group_order
    # hermitian_structure
    # kiss/kissing number/kissing_number/kissing_numbewr
    # magma
    # minimum/minimal norm/minimal_norm
    # minvecs
    # modular
    # name/namb
    # orbits
    # properties
    # reference/references
    # root_system
    # similarity
    # subgroup
    # subgroup_generators
    # subgroup_name
    # subgroup_order
    # theta/theta_series
    # triangular_basis
    # unimodular
    # url (parenthetical)
    # comments/notes/remarks

    # Properties (capitalization inconsistent, spacing around equal sign inconsistent, sometimes period at end, one parenthetical occurence)

    # N-modular extremal.
    # Extremal N-modular lattice.
    # EVEN=1
    # EXTREMAL=1
    # HermitianUnimodular=1
    # UnimodularHermitian=1
    # INTEGRAL=0
    # INTEGRAL=1
    # MODULAR=N (N can be 0)
    # UNIMODULAR=1
    # Unimodular=1, Extremal=1
    # integral,even

    parser = SectionExtractor()
    with open(fname) as F:
        parser.feed(F.read())
    return parser.data.get("properties", [])

parsers = {
    "Borch25.html": Borch25,
    "even_det2.25.html": Even25,
    "perfect-forms-dim8.txt": perfect8,
    "Brandt_2.html": Brandt2,
    "Brandt_1.html": Brandt1,
    "Jagy.txt": Jagy,
}
for fname in ['d1080.html', 'd1161.html', 'd1236.html', 'd1308.html', 'd1373.html', 'd1433.html', 'd1492.html', 'd1549.html', 'd1604.html', 'd1656.html', 'd1705.html', 'd1732.html', 'd4to457.html', 'd641.html', 'd777.html', 'd893.html', 'd992.html']:
    parsers[fname] = Nipp4

for fname in ['tbl.256.html', 'tbl.270.html', 'tbl.300.html', 'tbl.322.html', 'tbl.345.html', 'tbl.400.html', 'tbl.440.html', 'tbl.480.html', 'tbl.500.html', 'tbl.513.html']:
    parsers[fname] = Nipp5

for fname in ['2_dim4.dat', '2_dim8.dat', '2_dim12.dat', '2_dim16.dat', '2_dim20.dat', '2_dim24.dat', '2_dim28.dat', '2_dim32.dat', '2_dim36.dat', '2_dim40.dat', '2_dim44.dat', '2_dim48.dat', '3_dim2.dat', '3_dim4.dat', '3_dim6.dat', '3_dim8.dat', '3_dim10.dat', '3_dim12.dat', '3_dim14.dat', '3_dim16.dat', '3_dim18.dat', '3_dim20.dat', '3_dim22.dat', '3_dim24.dat', '3_dim26.dat', '3_dim28.dat', '3_dim30.dat', '3_dim32.dat', '3_dim34.dat', '3_dim40.dat', '5_dim4.dat', '5_dim8.dat', '5_dim12.dat', '5_dim16.dat', '5_dim20.dat', '5_dim24.dat', '5_dim28.dat', '6_dim8.dat', '6_dim16.dat', '6_dim24.dat', '6a_dim4.dat', '6a_dim12.dat', '6b_dim4.dat', '6b_dim12.dat', '6b_dim20.dat', '7_dim2.dat', '7_dim4.dat', '7_dim6.dat', '7_dim8.dat', '7_dim10.dat', '7_dim14.dat', '7_dim16.dat', '7_dim20.dat', '11_dim10.dat', '11_dim2.dat', '11_dim4.dat', '11_dim6.dat', '11_dim8.dat', '14_dim12.dat', '14_dim4.dat', '14_dim8.dat', '15_dim4.dat', '15_dim8.dat', '15_dim12.dat', '15_dim16.dat', '23_dim2.dat', '23_dim4.dat']:
    parsers[fname] = ExtLat

for fname in ['dim42min4.html', 'dim54min5.html', 'dim38min4.html', 'dim36min4b.html']:
    parsers[fname] = magmabasis_to_gram

for fname in ['R43.html', 'HKO68.html', 'HKO44.html', 'HZ40.html', 'GH39.html', 'H47.html', 'H46.html', 'HKO60.html']:
    parsers[fname] = basis_to_gram

for fname in [
        "abbrev.html", # Abbreviations and overall format help

        "index.html",
        "perfect.html", # List of perfect lattices; should check that perfect is included in the corresponding property field
        "stronglyperfect.html", # Same for strongly perfect lattices
        "unimodular.html", # we should double check that this table is correct/complete and properties are correct
        "modular.html", # we should double check that this table is correct/complete and properties are correct

        "density.html", # has dimensions with entries but no links.  Should we have these lattices?

        "nipp.html", # Format description for nipp4
        "nipp5.html", # Format description for nipp5
        "ExtLat.html", # Format description for ExtLat

        "bacher.html", # defines a useful kind of polynomial
        "mod_foot.html", # Footnotes to modular.html
        "ext72.html", # Some notes about the extremal 72 dimensional unimodular lattice Gamma

        "app1732.html", # Genus info for nipp4
        "app1080.html", # Genus info for nipp4

        "stdtoMAGMA.txt", # std -> Magma script
        "stdtoMAPLE.txt", # std -> Maple script
        "stdtoGAP.txt", # std -> GAP script
        "stdtoMACSYMA.txt", # std -> Macsyma script
        "stdtoPARI.txt", # std -> Pari script
        "htmltostd.txt", # HTML -> std script
]:
    parsers[fname] = noop

def test_parsers(folder="/Users/roed/Downloads/Nebescrape/"):
    allkeys = set()
    for fname in os.listdir(folder):
        if fname not in parsers:
            keys = singleton(opj(folder, fname))
            allkeys.update(keys)
    return allkeys
