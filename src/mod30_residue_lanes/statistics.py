import numpy as np


def lane_density(values, interval_size):
    """Compute density of values across interval size."""

    return len(values) / interval_size


def lane_entropy(counts):
    """Shannon entropy for lane distributions."""

    counts = np.asarray(counts)

    if counts.sum() == 0:
        return 0.0

    probabilities = counts / counts.sum()
    probabilities = probabilities[probabilities > 0]

    return -np.sum(probabilities * np.log2(probabilities))