[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/thinkthoughts/mod30-residue-lanes/blob/main/notebooks/00_mrl_foundations.ipynb)

# Report 00 — MRL Foundations

Modulo 30 defines eight admissible residue lanes before prime classification:

```text
01 → 07 → 11 → 13 → 17 → 19 → 23 → 29
```

Constraint view:

> MRL studies admissible residue classes as discrete constraint surfaces before prime/composite labeling.

## Generated outputs

- Wheel table CSV: <a href="../results/notebook00_mod30_wheel_table.csv">`results/notebook00_mod30_wheel_table.csv`</a>
- Admissible residue lanes CSV: <a href="../results/notebook00_admissible_residue_lanes.csv">`results/notebook00_admissible_residue_lanes.csv`</a>
- Foundation JSON: <a href="../results/notebook00_mrl_foundations.json">`results/notebook00_mrl_foundations.json`</a>
- Residue wheel figure: <a href="../figures/notebook00_mod30_residue_wheel.png">`figures/notebook00_mod30_residue_wheel.png`</a>

## Verification

- Modulus: `30`
- Declared admissible residues: `[1, 7, 11, 13, 17, 19, 23, 29]`
- Computed residues coprime to 30: `[1, 7, 11, 13, 17, 19, 23, 29]`
- Declared matches computed: `True`

## Admissible residue table

|   position | is_admissible   |   gcd_with_30 |   lane_label |
|-----------:|:----------------|--------------:|-------------:|
|          1 | True            |             1 |           01 |
|          7 | True            |             1 |           07 |
|         11 | True            |             1 |           11 |
|         13 | True            |             1 |           13 |
|         17 | True            |             1 |           17 |
|         19 | True            |             1 |           19 |
|         23 | True            |             1 |           23 |
|         29 | True            |             1 |           29 |

## Interpretation

- Modulo 30 removes multiples of 2, 3, and 5.
- Eight positions remain as admissible residue lanes.
- These lanes form the base MRL substrate for later lane-specific notebooks.
- Notebook 01 can begin with lane 1 as anchor behavior and compare it against the full eight-lane wheel.

## Next step

Notebook 01 — Lane Residue 1 should generate lane-local counts, spacing, interval statistics, and comparison against all eight admissible lanes.
