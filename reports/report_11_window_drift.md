# Report 11 — Window Drift: Rolling Prime-Lane Trajectories

Notebook 11 introduces rolling window drift after Notebook 01 established symmetry and Notebook 07 introduced prime-filtered asymmetry.

Constraint view:

> Window drift turns static lane counts into rolling eight-lane trajectories, revealing how prime-filtered structure changes under shifted observation boundaries.

## Generated outputs

- Rolling prime lane vectors CSV: <a href="../results/notebook11_rolling_prime_lane_vectors.csv">`results/notebook11_rolling_prime_lane_vectors.csv`</a>
- Rolling drift metrics CSV: <a href="../results/notebook11_rolling_drift_metrics.csv">`results/notebook11_rolling_drift_metrics.csv`</a>
- Lane 11 rolling similarity CSV: <a href="../results/notebook11_lane11_rolling_similarity.csv">`results/notebook11_lane11_rolling_similarity.csv`</a>
- Lane leadership summary CSV: <a href="../results/notebook11_lane_leadership_summary.csv">`results/notebook11_lane_leadership_summary.csv`</a>
- Summary JSON: <a href="../results/notebook11_window_drift_summary.json">`results/notebook11_window_drift_summary.json`</a>
- Figure: <a href="../figures/notebook11_rolling_prime_lane_vectors.png">`figures/notebook11_rolling_prime_lane_vectors.png`</a>
- Figure: <a href="../figures/notebook11_lane11_rolling_count.png">`figures/notebook11_lane11_rolling_count.png`</a>
- Figure: <a href="../figures/notebook11_all_lane_rolling_trajectories.png">`figures/notebook11_all_lane_rolling_trajectories.png`</a>
- Figure: <a href="../figures/notebook11_euclidean_drift_timeline.png">`figures/notebook11_euclidean_drift_timeline.png`</a>
- Figure: <a href="../figures/notebook11_cosine_drift_timeline.png">`figures/notebook11_cosine_drift_timeline.png`</a>
- Figure: <a href="../figures/notebook11_lane11_rolling_correlation.png">`figures/notebook11_lane11_rolling_correlation.png`</a>
- Figure: <a href="../figures/notebook11_lane_leadership_windows.png">`figures/notebook11_lane_leadership_windows.png`</a>

## Summary

| Metric | Value |
|---|---:|
| Modulus | 30 |
| Target lane | 11 |
| Interval max | 60000 |
| Window size | 3000 |
| Step size | 300 |
| Rolling windows | 191 |
| Admissible prime values | 6054 |
| Lane 11 prime values | 761 |
| Mean lane 11 rolling count | 37.549738 |
| Std lane 11 rolling count | 4.302244 |
| Mean Euclidean drift | 5.235084 |
| Max Euclidean drift | 10.862780 |
| Mean cosine drift | 0.00120012 |
| Max cosine drift | 0.00316894 |

## Lane 11 rolling similarity

|   target_lane |   comparison_lane |   cosine_similarity |   pearson_correlation |
|--------------:|------------------:|--------------------:|----------------------:|
|            11 |                01 |            0.994792 |              0.562645 |
|            11 |                07 |            0.994523 |              0.583913 |
|            11 |                11 |            1        |              1        |
|            11 |                13 |            0.995927 |              0.715171 |
|            11 |                17 |            0.993611 |              0.593448 |
|            11 |                19 |            0.99337  |              0.517157 |
|            11 |                23 |            0.99421  |              0.578251 |
|            11 |                29 |            0.994618 |              0.582586 |

## Lane leadership summary

|   leader_lane |   leadership_windows |   mean_leader_margin |
|--------------:|---------------------:|---------------------:|
|            01 |                   16 |              0.375   |
|            07 |                   43 |              1.25581 |
|            11 |                   16 |              1.3125  |
|            13 |                   22 |              1.63636 |
|            17 |                   23 |              3.34783 |
|            19 |                   24 |              1.33333 |
|            23 |                   19 |              2.26316 |
|            29 |                   28 |              1.85714 |

## Drift summary

|       |   euclidean_drift |   cosine_similarity_previous |   cosine_drift |   target_lane_count |   target_lane_share |
|:------|------------------:|-----------------------------:|---------------:|--------------------:|--------------------:|
| count |         190       |                190           |  190           |           190       |        190          |
| mean  |           5.23508 |                  0.9988      |    0.00120012  |            37.4684  |          0.125262   |
| std   |           1.3429  |                  0.000593201 |    0.000593201 |             4.17558 |          0.00801019 |
| min   |           1       |                  0.996831    |    4.34369e-05 |            28       |          0.0972222  |
| 25%   |           4.3589  |                  0.998428    |    0.000747121 |            35       |          0.120401   |
| 50%   |           5.38516 |                  0.998858    |    0.00114235  |            37       |          0.126345   |
| 75%   |           6.08276 |                  0.999253    |    0.00157168  |            40       |          0.130736   |
| max   |          10.8628  |                  0.999957    |    0.00316894  |            50       |          0.142361   |

## Interpretation

- Notebook 01 showed equal lane counts under complete modulo-30 cycles.
- Notebook 07 showed prime-filtered asymmetry under fixed windows.
- Notebook 11 turns prime-filtered counts into rolling trajectories.
- Drift metrics measure how much the eight-lane vector changes as observation boundaries move.
- Lane leadership summarizes which residue lane locally dominates a rolling prime-count window.
- Lane `11` becomes the first window-drift focal lane.

## Next step

Notebook 13 can study boundary effects: how local windows behave near pre-15 constraint boundary lane `13`.
