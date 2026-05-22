Table name: `lat_inclusions`

This stores inclusion relationships among lattices, up to composition with automorphisms on both the domain and the codomain.  Currently there are no completeness guarantees for this data.

| Column | Type | Description |
| --- | --- | --- |
| domain | text | label of the domain |
| codomain | text | label of the codomain |
| primitive | boolean | whether the inclusion is primitive; equivalence to quotient being torsion free and to the codomain being a direct sum of the domain and the quotient |
| quotient_invs | integer[] | elementary abelian invariants of the torsion of the quotient |
| domain_rank | smallint | rank of the domain |
| codomain_rank | smallint | rank of the codomain |
| quotient_rank | smallint | rank of the quotient |
| multiplicity | integer | the number of inclusions of this type (with given domain, codomain and quotient_invs) up to automorphism (note that this is difficult to compute, and probably not feasible when |
| orthogonal_complement | numeric[] | vectors within the codomain so that the domain is isometric to the complement of the lattice spanned by these vectors (only for primitive embeddings) |
| quotient_gens | numeric[] | a list of vectors v within the domain, each corresponding to an invariant m in the quotient_invs, so that adding the vectors v/m gives a lattice isometric to the codomain |
| images | numeric[] | A matrix A so that the inclusion is y = A*x in terms of the fixed bases for the domain and codomain |
