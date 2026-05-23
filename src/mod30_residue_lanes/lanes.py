from collections import defaultdict

from .residues import residue_lane


def partition_by_lane(values):
    """Partition values into modulo-30 residue lanes."""

    lanes = defaultdict(list)

    for value in values:
        lanes[residue_lane(value)].append(value)

    return dict(lanes)