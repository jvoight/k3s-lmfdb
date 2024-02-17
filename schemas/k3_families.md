Table name: `k3_families`

This table stores families of K3 surfaces, organized by their Picard lattice (indeed, the label is just taken from the label of the label).  They are rigidified by specifying an embedding of Pic(X) x T into II_{3,19} up to automorphism, which is often unique.

Question: Is the isomorphism class of the transcendental lattice determined by Pic(X)?

| Column    | Type    | Description    |
| ----------- | -------------- | --------------- |
| label | text | If there is a unique embedding for this pair of Pic(X) and T up to Aut(II_{3,19}), this is just the label of the Picard lattice.  If not, we append a counter enumerating the embeddings (TBD) |
| picard_lattice | text |  label of the indefinite lattice  isometric to Pic(X) |
| transcendental_lattice | text | label of the transcendental lattice (orthogonal complement of Pic(X) inside II_{3,19}) |
| polarized_lattice_genus | text |  label of the genus of the positive definite lattice L in the decomposition Pic(X) = U + L.  If there is no such decomposition, this field is null |
| embedding | integer[] | A 22 x 22 matrix, where the left 22 x k piece gives the embedding of the transcendental lattice into II_{3,19} and the right 22 x (22-k) piece gives the embedding of the of Pic(X) |
| num_fibrations | smallint | number of elliptic surfaces isomorphic to X |
| discriminant | integer | discriminant of Pic(X) |
| related_objects | jsonb | other objects related to X (such as modular forms, etc.  Dictionary with possible keys "cmf", "modcurve", "shimura" |
| parameter_space_ambient | text | the label of the ambient space of the parameter space as a toric variety|
| parameter_space_equations | text[] | equations describing the parameter space |
| parameter_space_description | text | description of the parameter space |
| parameter_space_dim | integer | dimension of the parameter space |
| moduli_space_dim | integer | dimension of the moduli space |
| moduli_space_unirational | boolean | whether the moduli space is unirational |
| moduli_space_kodaira_dimension | integer | The Kodaira dimension of the moduli space |
| fiber_dim | integer | dimension of the fiber to the moduli space |
| fiber_group | text | description of the automorphism group of the fiber |
| versal_family | text | The equation for a K3 surface corresponding to the generic point in the parameter space |
| specializations | text[] | picard_lattice labels for higher rank specializations |
| specialization_loci | text[] | list of lists of equations cutting out the loci where each specialization occurs |
| aut_group | integer[] | generators for the automorphism group of the family as matrices of dimension equal to the rank of the Picard lattice |