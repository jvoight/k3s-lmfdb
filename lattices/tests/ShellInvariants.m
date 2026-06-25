// Minimal-vector lattice invariants from connect_genus.m:
// IsWellRounded, IsStronglyWellRounded, IsMinimalVectorGenerated, IsEutactic,
// PerfectionDefect.

// --- IsStronglyWellRounded -------------------------------------------------
for tup in [* <Lattice("A",2), true>, <Lattice("A",3), true>, <Lattice("D",4), true>,
              <Lattice("D",5), true>, <Lattice("E",6), true>, <Lattice("E",8), true>,
              <StandardLattice(3), true>,
              <LatticeWithGram(DiagonalMatrix(Rationals(),[1,2,3])), false> *] do
    L := tup[1];
    assert IsStronglyWellRounded(L, ShortestVectors(L)) eq tup[2];
end for;
// rank-6 lattice that is well rounded but NOT strongly well rounded
G6 := SymmetricMatrix(Rationals(), [55, 1,19, 36,0,55, -1,-3,-37,46, 7,3,7,0,6, -20,6,-35,29,1,31]);
L6 := LatticeWithGram(G6);  S6 := ShortestVectors(L6);
assert IsWellRounded(L6, S6);
assert not IsStronglyWellRounded(L6, S6);

// --- IsEutactic (with exact certificate) -----------------------------------
for L in [ StandardLattice(3), Lattice("A",2), Lattice("A",3), Lattice("D",4),
           Lattice("E",6), Lattice("E",8) ] do
    S := ShortestVectors(L);
    eu, coeffs := IsEutactic(L, S);
    assert eu;
    assert #coeffs eq #S and forall{ c : c in coeffs | c gt 0 };
    G := ChangeRing(GramMatrix(L), Rationals());
    U := [ Vector(Rationals(), [ x : x in Coordinates(L, s) ]) : s in S ];
    M := &+[ coeffs[i] * (Transpose(Matrix(U[i])) * Matrix(U[i])) : i in [1..#U] ];
    assert M eq G^-1;          // sum_s c_s u_s^t u_s = G^{-1}, c_s > 0
end for;
// well rounded but not (weakly) eutactic, and a non-well-rounded lattice
Lne := LatticeWithGram(Matrix(Rationals(),2,2,[2,1/2,1/2,2]));
assert not IsEutactic(Lne, ShortestVectors(Lne));
Lnw := LatticeWithGram(DiagonalMatrix(Rationals(),[1,2,3]));
assert not IsEutactic(Lnw, ShortestVectors(Lnw));

// --- PerfectionDefect / IsMinimalVectorGenerated ---------------------------
assert PerfectionDefect(Lattice("E",8), ShortestVectors(Lattice("E",8))) eq 0;   // perfect
assert PerfectionDefect(Lattice("A",2), ShortestVectors(Lattice("A",2))) eq 0;   // perfect
assert PerfectionDefect(Lattice("A",3), ShortestVectors(Lattice("A",3))) eq 0;   // perfect
assert IsMinimalVectorGenerated(Lattice("E",8), ShortestVectors(Lattice("E",8)));
assert IsMinimalVectorGenerated(Lattice("A",3), ShortestVectors(Lattice("A",3)));
