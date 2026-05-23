# Report 29 — Sparse Feature Emergence at the Reset Boundary

Notebook 29 studies sparse transition behavior near the modulo-30 reset boundary:

```text
23 → 29 → 01
```

## Generated outputs

- Feature matrix CSV: <a href="../results/notebook29_reset_feature_matrix.csv">`results/notebook29_reset_feature_matrix.csv`</a>
- Sparse events CSV: <a href="../results/notebook29_sparse_events.csv">`results/notebook29_sparse_events.csv`</a>
- Reset state counts CSV: <a href="../results/notebook29_reset_state_counts.csv">`results/notebook29_reset_state_counts.csv`</a>
- Summary JSON: <a href="../results/notebook29_reset_summary.json">`results/notebook29_reset_summary.json`</a>
- Figure: <a href="../figures/notebook29_reset_lane_counts.png">`figures/notebook29_reset_lane_counts.png`</a>
- Figure: <a href="../figures/notebook29_reset_pressure.png">`figures/notebook29_reset_pressure.png`</a>
- Figure: <a href="../figures/notebook29_sparse_feature_heatmap.png">`figures/notebook29_sparse_feature_heatmap.png`</a>
- Figure: <a href="../figures/notebook29_sparse_event_timeline.png">`figures/notebook29_sparse_event_timeline.png`</a>
- Figure: <a href="../figures/notebook29_reset_state_counts.png">`figures/notebook29_reset_state_counts.png`</a>
- Figure: <a href="../figures/notebook29_reset_boundary_graph.png">`figures/notebook29_reset_boundary_graph.png`</a>

## Summary

| Metric | Value |
|---|---:|
| Windows | 3714 |
| Sparse events | 289 |
| Mean reset pressure | 0.050477 |
| Max reset pressure | 0.230769 |
| Mean boundary pressure | 0.052321 |
| Max boundary pressure | 0.265306 |

## State Counts

| state      |   count |
|:-----------|--------:|
| balanced   |    1898 |
| 29-leading |     745 |
| 01-leading |     679 |
| 23-leading |     392 |

## Interpretation

Lane 29 behaves as the final admissible residue state before modulo-30 reset into lane 01.

Sparse transition events emerge when:

- lane 29 separates from lane 01,
- reset pressure increases,
- local boundary imbalance forms between lanes 23 and 29.

The resulting feature system forms a sparse transition manifold near the modulo reset boundary.
