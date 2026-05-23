# Report 01 — Lane Residue 1

Notebook 01 begins lane-specific MRL analysis with residue lane `01`.

## Notebook 01

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/thinkthoughts/mod30-residue-lanes/blob/main/notebooks/01_lane_residue_1.ipynb)

Constraint view:

> Lane 01 acts as the anchor lane for comparing admissible modulo-30 structure before prime/composite labeling.

## Generated outputs

- Lane counts CSV: <a href="../results/notebook01_lane_counts.csv">`results/notebook01_lane_counts.csv`</a>
- Lane 01 spacing CSV: <a href="../results/notebook01_lane01_spacing.csv">`results/notebook01_lane01_spacing.csv`</a>
- Window lane vectors CSV: <a href="../results/notebook01_window_lane_vectors.csv">`results/notebook01_window_lane_vectors.csv`</a>
- Lane 01 similarity CSV: <a href="../results/notebook01_lane01_similarity.csv">`results/notebook01_lane01_similarity.csv`</a>
- Summary JSON: <a href="../results/notebook01_lane_residue_1_summary.json">`results/notebook01_lane_residue_1_summary.json`</a>
- Figure: <a href="../figures/notebook01_admissible_lane_counts.png">`figures/notebook01_admissible_lane_counts.png`</a>
- Figure: <a href="../figures/notebook01_lane01_positions.png">`figures/notebook01_lane01_positions.png`</a>
- Figure: <a href="../figures/notebook01_lane01_spacing_distribution.png">`figures/notebook01_lane01_spacing_distribution.png`</a>
- Figure: <a href="../figures/notebook01_window_lane_vectors.png">`figures/notebook01_window_lane_vectors.png`</a>
- Figure: <a href="../figures/notebook01_lane01_similarity.png">`figures/notebook01_lane01_similarity.png`</a>

## Summary

| Metric | Value |
|---|---:|
| Modulus | 30 |
| Target lane | 01 |
| Total interval values | 3000 |
| Admissible values | 800 |
| Lane 01 values | 100 |
| Lane 01 density in full interval | 0.033333 |
| Lane 01 density among admissible values | 0.125000 |
| Mean lane 01 spacing | 30.000000 |

## Lane counts

|   residue |   count |   lane_label |   density_in_full_interval |   density_among_admissible | is_target_lane   |
|----------:|--------:|-------------:|---------------------------:|---------------------------:|:-----------------|
|         1 |     100 |           01 |                  0.0333333 |                      0.125 | True             |
|         7 |     100 |           07 |                  0.0333333 |                      0.125 | False            |
|        11 |     100 |           11 |                  0.0333333 |                      0.125 | False            |
|        13 |     100 |           13 |                  0.0333333 |                      0.125 | False            |
|        17 |     100 |           17 |                  0.0333333 |                      0.125 | False            |
|        19 |     100 |           19 |                  0.0333333 |                      0.125 | False            |
|        23 |     100 |           23 |                  0.0333333 |                      0.125 | False            |
|        29 |     100 |           29 |                  0.0333333 |                      0.125 | False            |

## Lane 01 spacing summary

|   count |   mean |   std |   min |   25% |   50% |   75% |   max |   unique_spacings |
|--------:|-------:|------:|------:|------:|------:|------:|------:|------------------:|
|      99 |     30 |     0 |    30 |    30 |    30 |    30 |    30 |                30 |

## Lane 01 similarity

|   target_lane |   comparison_lane |   cosine_similarity |
|--------------:|------------------:|--------------------:|
|            01 |                01 |                   1 |
|            01 |                07 |                   1 |
|            01 |                11 |                   1 |
|            01 |                13 |                   1 |
|            01 |                17 |                   1 |
|            01 |                19 |                   1 |
|            01 |                23 |                   1 |
|            01 |                29 |                   1 |

## Interpretation

- Lane `01` is one of eight admissible modulo-30 residue lanes.
- Across complete modulo-30 cycles, each admissible lane appears with equal count.
- Lane `01` repeats every 30 integers in the full integer stream.
- Window vectors give a reusable eight-lane representation for later MRL, CGCS, and correlation analysis.

## Next step

Notebook 07 can compare lane `07` against lane `01` and begin asymmetric-lift analysis across the residue spine.
