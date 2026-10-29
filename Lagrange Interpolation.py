"""Lagrange polynomial interpolation."""


def lagrange_interpolation(x_values, y_values, x):
    """Return the interpolated value at ``x``.

    ``x_values`` must contain distinct x-coordinates and have the same
    length as ``y_values``.
    """
    if len(x_values) != len(y_values):
        raise ValueError("x_values and y_values must have the same length")
    if len(set(x_values)) != len(x_values):
        raise ValueError("x_values must be distinct")
    if not x_values:
        raise ValueError("at least one data point is required")

    result = 0
    for i, (x_i, y_i) in enumerate(zip(x_values, y_values)):
        basis = 1
        for j, x_j in enumerate(x_values):
            if i != j:
                basis *= (x - x_j) / (x_i - x_j)
        result += y_i * basis
    return result


if __name__ == "__main__":
    x_values = [0, 1, 2]
    y_values = [1, 3, 7]
    print(lagrange_interpolation(x_values, y_values, 1.5))