Name: `k3_polarized`

This table stores individual polarized K3 surfaces, given as concrete models (e.g. a double cover of P2 ramified along a plane sextic; a quartic hypersurface in P3; or an elliptic surface).

| Column | Type | Description |
| --- | --- | --- |
| surface_label | text | label for the abstract K3 surface |
| degree | smallint | the degree of the embedding type? |
| picard_lattice | text | label for Pic(X) as a lattice |
| ambient_space | text | label for the ambient toric variety |
| equations | text[] | Equations |
| short_vectors | ? | Lines or conics (or twisted cubics, elliptic curves) that are effective generators for Pic(X) |
| curve_counts | integer[] | the number of smooth rational curves of degree 1, 2, 3,... |
| family_sources | text[] | toric/elliptic surface labels for families in which this model occurs |