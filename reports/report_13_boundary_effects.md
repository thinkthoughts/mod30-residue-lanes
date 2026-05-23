# Report 13 — Boundary Effects: Pre-15 Prime-Lane Pressure

Notebook 13 studies lane `13` as a pre-15 boundary lane and compares it against reflected lane `17`.

Constraint view:

> Lane 13 marks a pre-15 boundary position where rolling prime-lane trajectories can be compared against reflected post-15 behavior.

## Generated outputs

- Boundary rolling vectors CSV: <a href="../results/notebook13_boundary_rolling_vectors.csv">`results/notebook13_boundary_rolling_vectors.csv`</a>
- Boundary drift metrics CSV: <a href="../results/notebook13_boundary_drift_metrics.csv">`results/notebook13_boundary_drift_metrics.csv`</a>
- Boundary pair similarity CSV: <a href="../results/notebook13_boundary_pair_similarity.csv">`results/notebook13_boundary_pair_similarity.csv`</a>
- Boundary leadership summary CSV: <a href="../results/notebook13_boundary_leadership_summary.csv">`results/notebook13_boundary_leadership_summary.csv`</a>
- Summary JSON: <a href="../results/notebook13_boundary_effects_summary.json">`results/notebook13_boundary_effects_summary.json`</a>
- Figure: <a href="../figures/notebook13_boundary_rolling_prime_lane_vectors.png">`figures/notebook13_boundary_rolling_prime_lane_vectors.png`</a>
- Figure: <a href="../figures/notebook13_lane13_vs_lane17.png">`figures/notebook13_lane13_vs_lane17.png`</a>
- Figure: <a href="../figures/notebook13_reflection_gap_13_17.png">`figures/notebook13_reflection_gap_13_17.png`</a>
- Figure: <a href="../figures/notebook13_pre_post_boundary_imbalance.png">`figures/notebook13_pre_post_boundary_imbalance.png`</a>
- Figure: <a href="../figures/notebook13_boundary_reflection_pressure.png">`figures/notebook13_boundary_reflection_pressure.png`</a>
- Figure: <a href="../figures/notebook13_boundary_vector_drift.png">`figures/notebook13_boundary_vector_drift.png`</a>
- Figure: <a href="../figures/notebook13_boundary_leadership_windows.png">`figures/notebook13_boundary_leadership_windows.png`</a>

## Summary

| Metric | Value |
|---|---:|
| Modulus | 30 |
| Target lane | 13 |
| Reflected lane | 17 |
| Interval max | 90000 |
| Window size | 3000 |
| Step size | 300 |
| Rolling windows | 291 |
| Admissible prime values | 8710 |
| Lane 13 prime values | 1093 |
| Lane 17 prime values | 1097 |
| Mean boundary imbalance | -0.051546 |
| Mean boundary pressure | 0.024794 |
| Mean reflection gap 13 − 17 | -0.158076 |
| Mean reflection pressure | 0.051315 |

## Boundary pair similarity

|   lane_a |   lane_b |   cosine_similarity |   pearson_correlation |   mean_lane13_count |   mean_lane17_count |   mean_reflection_gap_13_17 |   mean_reflection_abs_gap_13_17 |   mean_reflection_pressure |
|---------:|---------:|--------------------:|----------------------:|--------------------:|--------------------:|----------------------------:|--------------------------------:|---------------------------:|
|       13 |       17 |            0.992264 |              0.520855 |             36.0722 |             36.2302 |                   -0.158076 |                         3.63574 |                  0.0513154 |

## Boundary leadership summary

|   leader_lane |   leadership_windows |   mean_leader_count |
|--------------:|---------------------:|--------------------:|
|            01 |                   27 |             39.3333 |
|            07 |                   57 |             39.5965 |
|            11 |                   32 |             40.5    |
|            13 |                   34 |             39.9706 |
|            17 |                   42 |             41.2619 |
|            19 |                   36 |             40.6389 |
|            23 |                   26 |             40.1154 |
|            29 |                   37 |             41.8378 |

## Boundary metric summary

|       |   boundary_imbalance |   boundary_pressure |   reflection_gap_13_17 |   reflection_pressure |
|:------|---------------------:|--------------------:|-----------------------:|----------------------:|
| count |          291         |         291         |             291        |           291         |
| mean  |           -0.0515464 |           0.0247943 |              -0.158076 |             0.0513154 |
| std   |            8.40202   |           0.0165513 |               4.54204  |             0.0388988 |
| min   |          -24         |           0         |             -11        |             0         |
| 25%   |           -6.5       |           0.0111524 |              -3        |             0.0149254 |
| 50%   |            0         |           0.0215827 |               0        |             0.0447761 |
| 75%   |            6         |           0.0339879 |               3        |             0.0769231 |
| max   |           20         |           0.0869565 |              10        |             0.16129   |

## Interpretation

- Notebook 13 treats lane `13` as the pre-15 boundary lane.
- Lane `17` is used as the reflected post-15 comparison lane.
- Boundary imbalance measures aggregate pre-boundary vs post-boundary prime occupancy.
- Reflection pressure measures how sharply lane `13` diverges from lane `17`.
- Boundary drift measures how the full eight-lane vector changes while this central split is tracked.

## Next step

Notebook 17 can study reflected-lane behavior directly: lane `17` as the post-15 partner of lane `13`.
