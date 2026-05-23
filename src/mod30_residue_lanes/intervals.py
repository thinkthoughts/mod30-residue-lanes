def interval(start, stop, step=1):
    """Generate integer interval."""

    return list(range(start, stop, step))


def interval_windows(values, window_size):
    """Yield sliding windows across a sequence."""

    for i in range(0, len(values), window_size):
        yield values[i:i + window_size]