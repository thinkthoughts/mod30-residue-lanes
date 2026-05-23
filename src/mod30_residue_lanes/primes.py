from .residues import admissible_mod30


def admissible_primes(limit):
    """Return admissible prime candidates up to limit."""

    return [
        n
        for n in range(2, limit + 1)
        if admissible_mod30(n) or n in [2, 3, 5]
    ]