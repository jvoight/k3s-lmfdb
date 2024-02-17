Table name: `lat_genera`

This table stores lattices (free Z-modules with a nondegenerate symmetric inner product) up to local equivalence (also refered to as the genus of the lattice).

| Column | Type | Description |
| --- | --- | --- |
| [label](https://beta.lmfdb.org/Lattice/Labels) | text | The part of the label that is constant across a genus |
| [rank](https://beta.lmfdb.org/knowledge/show/lattice.dimension) | smallint | the rank of the lattice |
| signature | smallint | the number of positive diagonal entries over R, so that a positive definite lattice has signature equal to dimension |
| [class_number](https://beta.lmfdb.org/knowledge/show/lattice.class_number) | smallint | size of the genus |
| [det](https://beta.lmfdb.org/knowledge/show/lattice.determinant) | bigint | determinant of Gram matrix |
| disc | bigint | the discriminant (close to the determinant, but off by a factor of 2 in some cases) |
| conway_symbol | text | the Conway symbol for the genus |
| [level](https://beta.lmfdb.org/knowledge/show/lattice.level) | bigint | level of lattice |
| is_even | boolean | whether the lattice is even |
| discriminant_group_invs | integer[] | Smith-style invariants for the discriminant group |
| discriminant_form | integer[] | Quadratic form on the discriminant group, as a symmetric matrix |
| adjacency_matrix | jsonb | A dictionary with primes as keys and flattened p-neighbor multi-edge adjaceny matrix as values |
| adjacency_polynomials | jsonb | A dictionary with primes as keys and factored characteristic polynomials of adjacency matrices as values (as a list of pairs (f,e) with f a list of integer coefficients and e an exponent) |
| mass | numeric[] | numerator and denominator of the mass (sum of 1/Aut(L) for L in the genus) |
