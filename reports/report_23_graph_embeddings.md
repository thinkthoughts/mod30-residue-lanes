# Report 23 — Graph Embeddings of Residue-Lane Manifolds

Notebook 23 treats residue lanes as graph nodes and rolling prime-lane correlations as weighted edges.

Constraint view:

> Residue lanes become a graph manifold when rolling prime-lane trajectories define weighted relationships between lanes.

## Generated outputs

- Rolling prime lane vectors CSV: <a href="../results/notebook23_rolling_prime_lane_vectors.csv">`results/notebook23_rolling_prime_lane_vectors.csv`</a>
- Graph nodes CSV: <a href="../results/notebook23_lane_graph_nodes.csv">`results/notebook23_lane_graph_nodes.csv`</a>
- Graph edges CSV: <a href="../results/notebook23_lane_graph_edges.csv">`results/notebook23_lane_graph_edges.csv`</a>
- Adjacency matrix CSV: <a href="../results/notebook23_graph_adjacency_matrix.csv">`results/notebook23_graph_adjacency_matrix.csv`</a>
- Laplacian matrix CSV: <a href="../results/notebook23_graph_laplacian_matrix.csv">`results/notebook23_graph_laplacian_matrix.csv`</a>
- Laplacian embedding CSV: <a href="../results/notebook23_laplacian_embedding.csv">`results/notebook23_laplacian_embedding.csv`</a>
- Graph modes CSV: <a href="../results/notebook23_graph_laplacian_modes.csv">`results/notebook23_graph_laplacian_modes.csv`</a>
- Graph signal mode scores CSV: <a href="../results/notebook23_graph_signal_mode_scores.csv">`results/notebook23_graph_signal_mode_scores.csv`</a>
- Summary JSON: <a href="../results/notebook23_graph_embedding_summary.json">`results/notebook23_graph_embedding_summary.json`</a>
- Figure: <a href="../figures/notebook23_graph_adjacency_matrix.png">`figures/notebook23_graph_adjacency_matrix.png`</a>
- Figure: <a href="../figures/notebook23_lane_correlation_matrix.png">`figures/notebook23_lane_correlation_matrix.png`</a>
- Figure: <a href="../figures/notebook23_laplacian_embedding.png">`figures/notebook23_laplacian_embedding.png`</a>
- Figure: <a href="../figures/notebook23_node_centrality.png">`figures/notebook23_node_centrality.png`</a>
- Figure: <a href="../figures/notebook23_sorted_edge_weights.png">`figures/notebook23_sorted_edge_weights.png`</a>
- Figure: <a href="../figures/notebook23_graph_mode_1_loadings.png">`figures/notebook23_graph_mode_1_loadings.png`</a>
- Figure: <a href="../figures/notebook23_graph_mode_2_loadings.png">`figures/notebook23_graph_mode_2_loadings.png`</a>
- Figure: <a href="../figures/notebook23_graph_mode_3_loadings.png">`figures/notebook23_graph_mode_3_loadings.png`</a>
- Figure: <a href="../figures/notebook23_graph_signal_mode_scores.png">`figures/notebook23_graph_signal_mode_scores.png`</a>
- Figure: <a href="../figures/notebook23_lane_similarity_graph.png">`figures/notebook23_lane_similarity_graph.png`</a>

## Summary

| Metric | Value |
|---|---:|
| Modulus | 30 |
| Target lane | 23 |
| Rolling windows | 491 |
| Graph nodes | 8 |
| Graph edges | 28 |
| Mean edge weight | 0.816627 |
| Max edge weight | 0.858706 |
| Min edge weight | 0.774242 |
| Target lane weighted degree | 5.741805 |

## Graph nodes

|   lane |   residue |   weighted_degree |   mean_prime_count |   std_prime_count |   strongest_neighbor |   strongest_neighbor_weight | is_target_lane   | laplacian_community   |
|-------:|----------:|------------------:|-------------------:|------------------:|---------------------:|----------------------------:|:-----------------|:----------------------|
|     01 |         1 |           5.70018 |            34.1487 |           4.22632 |                   17 |                    0.858706 | False            | A                     |
|     07 |         7 |           5.71341 |            34.6721 |           4.39408 |                   23 |                    0.844152 | False            | B                     |
|     11 |        11 |           5.73939 |            34.6721 |           4.24749 |                   07 |                    0.835555 | False            | B                     |
|     13 |        13 |           5.75104 |            34.3381 |           4.72758 |                   29 |                    0.84204  | False            | A                     |
|     17 |        17 |           5.73623 |            34.3259 |           4.90269 |                   01 |                    0.858706 | False            | A                     |
|     19 |        19 |           5.66439 |            34.1792 |           4.43469 |                   23 |                    0.840117 | False            | B                     |
|     23 |        23 |           5.7418  |            34.554  |           4.56126 |                   07 |                    0.844152 | True             | B                     |
|     29 |        29 |           5.68468 |            34.4582 |           4.79645 |                   13 |                    0.84204  | False            | A                     |

## Strongest graph edges

|   source |   target |   weight |   correlation |   cosine_similarity |   covariance |
|---------:|---------:|---------:|--------------:|--------------------:|-------------:|
|       01 |       17 | 0.858706 |      0.600589 |            0.992888 |     12.4698  |
|       07 |       23 | 0.844152 |      0.559114 |            0.992732 |     11.229   |
|       13 |       29 | 0.84204  |      0.535394 |            0.991263 |     12.1652  |
|       19 |       23 | 0.840117 |      0.545241 |            0.99234  |     11.0515  |
|       07 |       11 | 0.835555 |      0.540948 |            0.992973 |     10.1168  |
|       11 |       23 | 0.831497 |      0.523326 |            0.992371 |     10.1596  |
|       13 |       17 | 0.829795 |      0.495232 |            0.990253 |     11.5018  |
|       13 |       23 | 0.828673 |      0.501052 |            0.991079 |     10.8266  |
|       07 |       13 | 0.820087 |      0.478878 |            0.991006 |      9.96823 |
|       11 |       29 | 0.819932 |      0.48073  |            0.99116  |      9.81383 |
|       17 |       29 | 0.818001 |      0.457702 |            0.989422 |     10.7851  |
|       17 |       19 | 0.817734 |      0.466435 |            0.99021  |     10.1619  |

## Community summary

| laplacian_community   | lanes          |   mean_weighted_degree |   count |
|:----------------------|:---------------|-----------------------:|--------:|
| A                     | 01, 13, 17, 29 |                5.71803 |       4 |
| B                     | 07, 11, 19, 23 |                5.71475 |       4 |

## Interpretation

- Notebook 19 studied temporal spectral dynamics.
- Notebook 23 converts rolling lane trajectories into a weighted graph.
- Nodes are admissible residue lanes.
- Edges encode trajectory similarity, cosine alignment, and covariance strength.
- Laplacian embedding turns lane relationships into a learned graph geometry.
- Graph signal modes describe how rolling prime-count activity moves across graph eigenmodes.

## Next step

Notebook 29 can study sparse feature emergence and boundary-reset behavior on top of this graph manifold.
