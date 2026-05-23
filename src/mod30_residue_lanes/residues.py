ADMISSIBLE_RESIDUES = [1, 7, 11, 13, 17, 19, 23, 29]


def residue_lane(n: int) -> int:
    """Return modulo-30 residue lane."""
    return n % 30


def admissible_mod30(n: int) -> bool:
    """Check whether n belongs to an admissible modulo-30 lane."""
    return residue_lane(n) in ADMISSIBLE_RESIDUES