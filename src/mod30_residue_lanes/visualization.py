import matplotlib.pyplot as plt


def plot_lane_counts(lane_counts):
    """Bar plot for residue lane counts."""

    lanes = sorted(lane_counts.keys())
    counts = [lane_counts[l] for l in lanes]

    fig, ax = plt.subplots(figsize=(8, 4))

    ax.bar(lanes, counts)

    ax.set_xlabel("Residue Lane")
    ax.set_ylabel("Count")
    ax.set_title("Modulo-30 Residue Lane Counts")

    return fig, ax