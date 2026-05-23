# Report 17 — Reflected Manifold Decomposition

Notebook 17 treats lane `17` as the post-15 reflected lane and decomposes rolling prime-lane vectors into covariance and spectral modes.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/thinkthoughts/mod30-residue-lanes/blob/main/notebooks/17_lane_residue_17.ipynb)

Constraint view:

> Lane 17 anchors the reflected side of the mod30 residue manifold, where rolling prime-lane trajectories can be decomposed into shared modes, reflected modes, and local deviations.

## Generated outputs

- Rolling prime lane vectors CSV: <a href="../results/notebook17_rolling_prime_lane_vectors.csv">`results/notebook17_rolling_prime_lane_vectors.csv`</a>
- Spectral modes CSV: <a href="../results/notebook17_spectral_modes.csv">`results/notebook17_spectral_modes.csv`</a>
- Lane covariance matrix CSV: <a href="../results/notebook17_lane_covariance_matrix.csv">`results/notebook17_lane_covariance_matrix.csv`</a>
- Lane correlation matrix CSV: <a href="../results/notebook17_lane_correlation_matrix.csv">`results/notebook17_lane_correlation_matrix.csv`</a>
- Low-rank reconstruction CSV: <a href="../results/notebook17_low_rank_reconstruction.csv">`results/notebook17_low_rank_reconstruction.csv`</a>
- Mode scores CSV: <a href="../results/notebook17_mode_scores.csv">`results/notebook17_mode_scores.csv`</a>
- Lane 17 loading summary CSV: <a href="../results/notebook17_lane17_loading_summary.csv">`results/notebook17_lane17_loading_summary.csv`</a>
- Summary JSON: <a href="../results/notebook17_reflected_manifold_decomposition_summary.json">`results/notebook17_reflected_manifold_decomposition_summary.json`</a>
- Figure: <a href="../figures/notebook17_rolling_prime_lane_matrix.png">`figures/notebook17_rolling_prime_lane_matrix.png`</a>
- Figure: <a href="../figures/notebook17_lane_correlation_matrix.png">`figures/notebook17_lane_correlation_matrix.png`</a>
- Figure: <a href="../figures/notebook17_explained_variance.png">`figures/notebook17_explained_variance.png`</a>
- Figure: <a href="../figures/notebook17_eigenmode_1_loadings.png">`figures/notebook17_eigenmode_1_loadings.png`</a>
- Figure: <a href="../figures/notebook17_eigenmode_2_loadings.png">`figures/notebook17_eigenmode_2_loadings.png`</a>
- Figure: <a href="../figures/notebook17_eigenmode_3_loadings.png">`figures/notebook17_eigenmode_3_loadings.png`</a>
- Figure: <a href="../figures/notebook17_mode_scores.png">`figures/notebook17_mode_scores.png`</a>
- Figure: <a href="../figures/notebook17_low_rank_reconstruction_error.png">`figures/notebook17_low_rank_reconstruction_error.png`</a>
- Figure: <a href="../figures/notebook17_lane17_vs_lane13.png">`figures/notebook17_lane17_vs_lane13.png`</a>
- Figure: <a href="../figures/notebook17_reflection_gap_17_13.png">`figures/notebook17_reflection_gap_17_13.png`</a>

## Summary

| Metric | Value |
|---|---:|
| Modulus | 30 |
| Target lane | 17 |
| Reflected lane | 13 |
| Interval max | 120000 |
| Window size | 3000 |
| Step size | 300 |
| Rolling windows | 391 |
| Admissible prime values | 11298 |
| Lane 17 prime values | 1414 |
| Mode 1 explained variance | 0.560000 |
| Mode 2 explained variance | 0.096080 |
| Mode 3 explained variance | 0.084416 |
| First three modes cumulative explained variance | 0.740496 |
| Mean reflection gap 17 − 13 | -0.063939 |

## Spectral modes

|   mode |   eigenvalue |   explained_variance |   cumulative_explained_variance |   loading_01 |   loading_07 |   loading_11 |   loading_13 |   loading_17 |   loading_19 |   loading_23 |   loading_29 |
|-------:|-------------:|---------------------:|--------------------------------:|-------------:|-------------:|-------------:|-------------:|-------------:|-------------:|-------------:|-------------:|
|      1 |     92.4781  |            0.56      |                        0.56     |   -0.321125  |    -0.36319  |   -0.33917   |    -0.371431 |   -0.371187  |   -0.332488  |   -0.342409  |   -0.382626  |
|      2 |     15.8666  |            0.0960801 |                        0.65608  |    0.418035  |    -0.318793 |   -0.119475  |     0.184274 |    0.56561   |   -0.469615  |   -0.362037  |    0.062143  |
|      3 |     13.9403  |            0.0844156 |                        0.740496 |    0.0606616 |     0.342839 |    0.274122  |     0.182488 |   -0.503166  |   -0.583055  |   -0.195186  |    0.372975  |
|      4 |     11.3872  |            0.0689549 |                        0.809451 |   -0.0589777 |    -0.376651 |    0.107063  |    -0.244969 |   -0.0854303 |    0.388763  |   -0.419187  |    0.670097  |
|      5 |     10.5046  |            0.0636107 |                        0.873061 |   -0.219233  |    -0.533241 |    0.0439991 |     0.76603  |   -0.238356  |    0.0651701 |    0.129132  |   -0.0334292 |
|      6 |      8.60414 |            0.0521023 |                        0.925164 |   -0.108763  |     0.325495 |   -0.844215  |     0.260157 |   -0.0126863 |    0.0923386 |   -0.0907649 |    0.291404  |
|      7 |      7.27672 |            0.0440641 |                        0.969228 |    0.642082  |    -0.297297 |   -0.261422  |    -0.196514 |   -0.375513  |   -0.0419617 |    0.480618  |    0.136462  |
|      8 |      5.08168 |            0.030772  |                        1        |   -0.492753  |    -0.168468 |   -0.0332723 |    -0.20413  |    0.289563  |   -0.404089  |    0.531001  |    0.396156  |

## Low-rank reconstruction

|   modes_used |   frobenius_error |   relative_error |   explained_variance |
|-------------:|------------------:|-----------------:|---------------------:|
|            1 |     168.339       |       0.0850763  |             0.56     |
|            2 |     148.829       |       0.0752161  |             0.65608  |
|            3 |     129.28        |       0.0653363  |             0.740496 |
|            4 |     110.78        |       0.0559868  |             0.809451 |
|            5 |      90.4179      |       0.0456961  |             0.873061 |
|            6 |      69.4246      |       0.0350863  |             0.925164 |
|            7 |      44.518       |       0.0224989  |             0.969228 |
|            8 |       2.27845e-13 |       1.1515e-16 |             1        |

## Lane 17 loading summary

|   mode |   lane17_loading |   lane13_loading |   reflection_loading_gap_17_13 |   abs_lane17_loading |   explained_variance |
|-------:|-----------------:|-----------------:|-------------------------------:|---------------------:|---------------------:|
|      1 |       -0.371187  |        -0.371431 |                    0.000243924 |            0.371187  |            0.56      |
|      2 |        0.56561   |         0.184274 |                    0.381336    |            0.56561   |            0.0960801 |
|      3 |       -0.503166  |         0.182488 |                   -0.685654    |            0.503166  |            0.0844156 |
|      4 |       -0.0854303 |        -0.244969 |                    0.159539    |            0.0854303 |            0.0689549 |
|      5 |       -0.238356  |         0.76603  |                   -1.00439     |            0.238356  |            0.0636107 |
|      6 |       -0.0126863 |         0.260157 |                   -0.272843    |            0.0126863 |            0.0521023 |
|      7 |       -0.375513  |        -0.196514 |                   -0.178999    |            0.375513  |            0.0440641 |
|      8 |        0.289563  |        -0.20413  |                    0.493693    |            0.289563  |            0.030772  |

## Interpretation

- Notebook 13 measured boundary pressure around the `13 | 17` split.
- Notebook 17 treats lane `17` as a reflected post-15 anchor.
- Covariance and correlation matrices identify coupled lane neighborhoods.
- Eigenmodes expose shared and opposing components in rolling prime-lane trajectories.
- Low-rank reconstruction tests whether a few modes recover most observable structure.

## Next step

Notebook 19 can construct transition operators between rolling lane states and study lane-to-lane transition dynamics.
