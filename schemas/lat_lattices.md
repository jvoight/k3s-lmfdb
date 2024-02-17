Table name: `lat_lattices`

This table stores lattices (free Z-modules with a nondegenerate symmetric inner product) up to isomorphism.

Label: `dimension.signature.determinant.genus_spec.tiebreaker` where

- `genus_spec` is

  - ommitted if determinant is 1 and signature is not a multiple of 8
  - 0 for the even lattice and 1 for the odd in the case that determinant is 1 and signature is a multiple of 8
  - otherwise, for each p with p^2|determinant, we give the concatenated dimensions of the p,p^2,p^3... blocks in the Jordan decomposition (using lower case letters and then upper case letters if these dimensions are larger than 9; we separate different primes with periods.  Finally, we encode the rest of the genus information (sign, scale, oddity etc) into a single integer as described below, and append it to the Jordan information.  This integer will be even if the genus is even and odd if the genus is odd.
  - TODO for Eran: describe this encoding
  - For the tiebreaker, we use lexicographic sorting by canonical Gram matrix for definite lattices.  For indefinite lattices, a tiebreaker is only needed in rank 2 or 3 (in rank 3 spinor genera provide a complete invariant).

| Column | Type | Description |
| --- | --- | --- |
| [aut_size](https://beta.lmfdb.org/knowledge/show/lattice.group_order) | numeric | size of automorphism group |
| aut_label | text | label for the automorphism group as an abstract group |
| [rank](https://beta.lmfdb.org/knowledge/show/lattice.dimension) | smallint | the rank of the lattice |
| signature | smallint | the number of positive diagonal entries over R, so that a positive definite lattice has signature equal to dimension |
| [det](https://beta.lmfdb.org/knowledge/show/lattice.determinant) | bigint | determinant of Gram matrix |
| disc | bigint | the discriminant (close to the determinant, but off by a factor of 2 in some cases) |
| [class_number](https://beta.lmfdb.org/knowledge/show/lattice.class_number) | smallint | size of the genus |
| [density](https://beta.lmfdb.org/knowledge/show/lattice.density) | numeric | center density of the lattice centered sphere packing (only for definite lattices) |
| [hermite](https://beta.lmfdb.org/knowledge/show/lattice.hermite_number) | numeric | Hermite number (only for definite lattices) |
| [kissing](https://beta.lmfdb.org/knowledge/show/lattice.kissing) | bigint | kissing number (only for definite lattices) |
| [level](https://beta.lmfdb.org/knowledge/show/lattice.level) | bigint | level of lattice |
| [minimum](https://beta.lmfdb.org/knowledge/show/lattice.minimal_vector) | integer | length of shortest vector (only for definite lattices) |
| name | text | a string like "E8", often null |
| [theta_series](https://beta.lmfdb.org/knowledge/show/lattice.theta) | numeric[] | a vector, counting the number of representations of n (odd) or 2n (even) |
| [gram](https://beta.lmfdb.org/knowledge/show/lattice.gram) | integer[] | Gram matrix (in canonical form, so the knowl should be updated) |
| [label](https://beta.lmfdb.org/Lattice/Labels) | text | We're changing the label; see below |
| [genus_label](https://beta.lmfdb.org/Lattice/Labels) | text | The part of the label that is constant across a genus |
| conway_symbol | text | the Conway symbol for the genus |
| pneighbors | jsonb | a dictionary with primes as keys and a list of labels as values (the p-neighbors) |
| discriminant_group_invs | integer[] | Smith-style invariants for the discriminant group |
| festi_veniani_index | integer | the index of the lattice automorphism group within the automorphism group of the discriminant group |
| is_even | boolean | whether the lattice is even |
| dual_label | text | the label for the minimal integral scaling of the dual lattice (may be null if the discriminant is too large) |
| dual_theta_series | numeric[] | the theta series of the dual lattice |
| dual_hermite | numeric | the Hermite number of the dual lattice (only for definite lattices) |
| dual_kissing | bigint | the kissing number of the dual lattice (only for definite lattices) |
| dual_density | numeric | the center density of the dual lattice (only for definite lattices) |
| dual_det | bigint | the determinant of the dual lattice |
| dual_conway | text | the Conway symbol for the dual lattice |
