import numpy as np


def cosine_similarity(a, b):
    """Compute cosine similarity between vectors."""

    a = np.asarray(a)
    b = np.asarray(b)

    denominator = np.linalg.norm(a) * np.linalg.norm(b)

    if denominator == 0:
        return 0.0

    return float(np.dot(a, b) / denominator)


def correlation_matrix(vectors):
    """Compute pairwise cosine similarity matrix."""

    n = len(vectors)

    matrix = np.zeros((n, n))

    for i in range(n):
        for j in range(n):
            matrix[i, j] = cosine_similarity(
                vectors[i],
                vectors[j],
            )

    return matrix