ADMISSIBLE_RESIDUES = [1, 7, 11, 13, 17, 19, 23, 29]

def admissible_mod30(n: int) -> bool:
    return n % 30 in ADMISSIBLE_RESIDUES

def residue_lane(n: int) -> int:
    return n % 30