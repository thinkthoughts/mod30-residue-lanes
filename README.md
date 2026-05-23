# Mod30 Residue Lanes (MRL)

Modulo 30 produces eight admissible residue lanes:

1, 7, 11, 13, 17, 19, 23, 29

MRL studies these lanes as discrete constraint surfaces prior to prime classification.

## Residue Spine

01 → 07 → 11 → 13 → 17 → 19 → 23 → 29

## Notebook Map

| Notebook | Lane | Focus |
|---|---:|---|
| `01_lane_residue_1.ipynb` | 1 | anchor lane / identity behavior |
| `07_lane_residue_7.ipynb` | 7 | first asymmetric lift |
| `11_lane_residue_11.ipynb` | 11 | mid-wheel expansion |
| `13_lane_residue_13.ipynb` | 13 | pre-15 constraint boundary |
| `17_lane_residue_17.ipynb` | 17 | post-15 reflected lane |
| `19_lane_residue_19.ipynb` | 19 | mirrored expansion |
| `23_lane_residue_23.ipynb` | 23 | late-wheel lift |
| `29_lane_residue_29.ipynb` | 29 | boundary-before-reset lane |

## Repo Structure

```text
mod30-residue-lanes/
├── notebooks/
├── src/
├── data/
├── results/
├── figures/
└── docs/
```

## Initial Questions

- how do admissible residue lanes distribute?
- what structure emerges before prime labeling?
- how stable are lane-local statistics?
- can RML recover lane geometry from sparse observations?
- how do neighboring lanes correlate across intervals?

## License

MIT