Table name: `k3_elliptic`

This table stores K3 surfaces equipped with an elliptic fibration, which are parameterized by Picard lattices expressed as a direct sum U+L, where U is the rank 2 lattice with Gram matrix [0,1;0,-2] and L is a negative definite lattice.

They are labeled by the lattice label for L.

| Column |Type | Description |
| ---- | ---- | ---- |
| polarized_lattice | text | label of the positive definite lattice L<-1> |
| K3_family | text | label of the K3 family |
| mw_rank | smallint | rank of the Mordell-Weil group |
| mw_torsion | smallint[] | elementary divisors of the torsion of Mordell-Weil |
| reducible_fibers | text[] | a description of the reducible fibers, by name of the ADE lattices|
| multiplicity | integer | number of inequivalent fibrations with the same lattice L |
| mw_pairing |text | label of the quadratic form on Mordel-Weil, scaled to be integral|
| mw_denom | integer | scaling factor for mw_pairing |
| aut_group | integer[] | generators for the automorphism group of the elliptic fibration (automorphisms of the surface that preserve the fibration) |