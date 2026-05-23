# Report 07 — First Asymmetry: Prime-Filtered Lane Dynamics

Notebook 07 introduces the first asymmetry after Notebook 01 established the symmetric modulo-30 baseline.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/thinkthoughts/mod30-residue-lanes/blob/main/notebooks/07_lane_residue_7.ipynb)

Constraint view:

> Prime filtering breaks perfect admissible-lane symmetry and reveals lane-local structure beyond the modulo-30 substrate.

## Generated outputs

- Prime-filtered lane counts CSV: <a href="../results/notebook07_prime_filtered_lane_counts.csv">`results/notebook07_prime_filtered_lane_counts.csv`</a>
- Lane 07 prime spacing CSV: <a href="../results/notebook07_lane07_prime_spacing.csv">`results/notebook07_lane07_prime_spacing.csv`</a>
- Windowed prime lane vectors CSV: <a href="../results/notebook07_prime_window_lane_vectors.csv">`results/notebook07_prime_window_lane_vectors.csv`</a>
- Lane 07 prime similarity CSV: <a href="../results/notebook07_lane07_prime_similarity.csv">`results/notebook07_lane07_prime_similarity.csv`</a>
- Summary JSON: <a href="../results/notebook07_prime_filtered_lane_dynamics_summary.json">`results/notebook07_prime_filtered_lane_dynamics_summary.json`</a>
- Figure: <a href="../figures/notebook07_baseline_vs_prime_lane_counts.png">`figures/notebook07_baseline_vs_prime_lane_counts.png`</a>
- Figure: <a href="../figures/notebook07_prime_share_by_lane.png">`figures/notebook07_prime_share_by_lane.png`</a>
- Figure: <a href="../figures/notebook07_lane07_prime_positions.png">`figures/notebook07_lane07_prime_positions.png`</a>
- Figure: <a href="../figures/notebook07_lane07_prime_spacing_distribution.png">`figures/notebook07_lane07_prime_spacing_distribution.png`</a>
- Figure: <a href="../figures/notebook07_prime_window_lane_vectors.png">`figures/notebook07_prime_window_lane_vectors.png`</a>
- Figure: <a href="../figures/notebook07_lane07_prime_similarity.png">`figures/notebook07_lane07_prime_similarity.png`</a>
- Figure: <a href="../figures/notebook07_prime_count_delta_from_mean.png">`figures/notebook07_prime_count_delta_from_mean.png`</a>

## Summary

| Metric | Value |
|---|---:|
| Modulus | 30 |
| Target lane | 07 |
| Total interval values | 30000 |
| Admissible values | 8000 |
| Prime values | 3245 |
| Admissible prime values | 3242 |
| Lane 07 prime values | 407 |
| Asymmetry score std/mean | 0.011156 |
| Mean lane 07 prime spacing | 73.743842 |

## Prime-filtered lane counts

|   residue |   baseline_count |   prime_count |   lane_label |   prime_density_within_lane |   prime_share_among_admissible_primes |   prime_count_delta_from_mean | is_target_lane   |
|----------:|-----------------:|--------------:|-------------:|----------------------------:|--------------------------------------:|------------------------------:|:-----------------|
|         1 |             1000 |           402 |           01 |                       0.402 |                              0.123998 |                         -3.25 | False            |
|         7 |             1000 |           407 |           07 |                       0.407 |                              0.12554  |                          1.75 | True             |
|        11 |             1000 |           406 |           11 |                       0.406 |                              0.125231 |                          0.75 | False            |
|        13 |             1000 |           406 |           13 |                       0.406 |                              0.125231 |                          0.75 | False            |
|        17 |             1000 |           411 |           17 |                       0.411 |                              0.126774 |                          5.75 | False            |
|        19 |             1000 |           395 |           19 |                       0.395 |                              0.121838 |                        -10.25 | False            |
|        23 |             1000 |           408 |           23 |                       0.408 |                              0.125848 |                          2.75 | False            |
|        29 |             1000 |           407 |           29 |                       0.407 |                              0.12554  |                          1.75 | False            |

## Lane 07 prime spacing summary

|   count |    mean |    std |   min |   25% |   50% |   75% |   max |   unique_spacing_count |   min_spacing |   max_spacing |
|--------:|--------:|-------:|------:|------:|------:|------:|------:|-----------------------:|--------------:|--------------:|
|     406 | 73.7438 | 55.313 |    30 |    30 |    60 |    90 |   330 |                     11 |            30 |           330 |

## Lane 07 prime similarity

|   target_lane |   comparison_lane |   cosine_similarity |
|--------------:|------------------:|--------------------:|
|            07 |                01 |            0.996965 |
|            07 |                07 |            1        |
|            07 |                11 |            0.993564 |
|            07 |                13 |            0.996647 |
|            07 |                17 |            0.993481 |
|            07 |                19 |            0.994569 |
|            07 |                23 |            0.995552 |
|            07 |                29 |            0.997634 |

## Interpretation

- Notebook 01 showed the symmetric baseline of complete modulo-30 admissible cycles.
- Notebook 07 adds prime filtering as the first extra constraint.
- Prime filtering breaks equal lane occupancy while retaining the same eight-lane substrate.
- Lane `07` becomes the first asymmetric-lift notebook in the MRL sequence.
- Windowed prime-count vectors are now meaningful inputs for later RML, CGCS, and cross-lane correlation analysis.

## Next step

Notebook 11 can study window drift: how prime-filtered lane vectors change when window boundaries no longer align cleanly with modulo-30 cycles.
