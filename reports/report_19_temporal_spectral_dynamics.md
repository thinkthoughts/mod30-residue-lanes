# Report 19 — Temporal Spectral Dynamics of Residue Manifolds

Notebook 19 studies rolling eigenspace stability and temporal phase structure across mod30 residue manifolds.

## Generated outputs

- Rolling vectors CSV: <a href="../results/notebook19_rolling_vectors.csv">`results/notebook19_rolling_vectors.csv`</a>
- Spectral metrics CSV: <a href="../results/notebook19_rolling_spectral_metrics.csv">`results/notebook19_rolling_spectral_metrics.csv`</a>
- Eigenspace drift CSV: <a href="../results/notebook19_eigenspace_drift.csv">`results/notebook19_eigenspace_drift.csv`</a>
- Transition matrix CSV: <a href="../results/notebook19_transition_similarity_matrix.csv">`results/notebook19_transition_similarity_matrix.csv`</a>
- Phase embedding CSV: <a href="../results/notebook19_phase_embedding.csv">`results/notebook19_phase_embedding.csv`</a>
- Summary JSON: <a href="../results/notebook19_temporal_spectral_summary.json">`results/notebook19_temporal_spectral_summary.json`</a>
- Figure: <a href="../figures/notebook19_rolling_explained_variance.png">`figures/notebook19_rolling_explained_variance.png`</a>
- Figure: <a href="../figures/notebook19_spectral_entropy.png">`figures/notebook19_spectral_entropy.png`</a>
- Figure: <a href="../figures/notebook19_mode_rotation_angles.png">`figures/notebook19_mode_rotation_angles.png`</a>
- Figure: <a href="../figures/notebook19_eigenspace_cosine_drift.png">`figures/notebook19_eigenspace_cosine_drift.png`</a>
- Figure: <a href="../figures/notebook19_transition_heatmap.png">`figures/notebook19_transition_heatmap.png`</a>
- Figure: <a href="../figures/notebook19_phase_cluster_embedding.png">`figures/notebook19_phase_cluster_embedding.png`</a>
- Figure: <a href="../figures/notebook19_rolling_prime_manifold.png">`figures/notebook19_rolling_prime_manifold.png`</a>

## Summary

| Metric | Value |
|---|---:|
| Modulus | 30 |
| Rolling windows | 391 |
| Rolling spectral blocks | 371 |
| Mean spectral entropy | 1.342356 |
| Mean Mode 1 variance | 0.533861 |
| Mean Mode 2 variance | 0.229632 |
| Mean Mode 1 rotation | 9.814924 |
| Mean Mode 2 rotation | 18.875461 |

## Interpretation

- Rolling windows generate evolving residue manifolds.
- Local eigenspaces remain coherent but rotate gradually.
- Spectral entropy tracks manifold concentration vs fragmentation.
- Transition heatmaps reveal persistent temporal structure.
- Low-dimensional embeddings expose recurring manifold phases.

## Next step

Notebook 23 can introduce graph manifold embeddings and lane-transition operators.
