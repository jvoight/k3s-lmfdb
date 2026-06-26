// The three shell-design-strength methods in tdesign.m must agree (the cutoffs
// in tDesign only choose the fastest, so correctness is method-independent).
import "tdesign.m" : shell_design_strength,
                     shell_design_strength_harmonic,
                     shell_design_strength_Molien;

for tup in [* <Lattice("A",2), 5>, <Lattice("A",3), 3>, <Lattice("D",4), 5> *] do
    L := tup[1];  half := ShortestVectors(L);  A := AutomorphismGroup(L);
    assert shell_design_strength(L, half) eq tup[2];
    assert shell_design_strength_harmonic(L, half) eq tup[2];
    assert shell_design_strength_Molien(L, half, A) eq tup[2];
end for;

// The intrinsic itself (direct path): E8 minimal vectors are a 7-design.
assert tDesign(Lattice("E",8), ShortestVectors(Lattice("E",8))) eq 7;
