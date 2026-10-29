"""The primal simplex algorithm for linear programs in standard form.

Solves maximisation problems of the form:

    maximise     c @ x
    subject to   A @ x <= b
                 x >= 0

The constraints must have non-negative right-hand sides.  A tuple containing
the optimal value, decision variables, and final tableau is returned.
"""


def simplex(c, A, b, *, tolerance=1e-10):
    """Return ``(maximum, variables, tableau)`` using the primal simplex method.

    Raises:
        ValueError: if the input is malformed or the initial basic solution is
            infeasible.
        RuntimeError: if the objective is unbounded.
    """
    c = [float(value) for value in c]
    A = [[float(value) for value in row] for row in A]
    b = [float(value) for value in b]

    if not c or len(A) != len(b) or any(len(row) != len(c) for row in A):
        raise ValueError("A, b, and c have incompatible dimensions")
    if any(value < -tolerance for value in b):
        raise ValueError("the initial basic solution is infeasible")

    rows, columns = len(A), len(c)
    # Tableau columns are decision variables, slack variables, then RHS.
    tableau = [
        row[:] + [1.0 if i == j else 0.0 for j in range(rows)] + [rhs]
        for i, (row, rhs) in enumerate(zip(A, b))
    ]
    tableau.append([-value for value in c] + [0.0] * (rows + 1))

    while True:
        objective = tableau[-1]
        entering = min(
            range(columns + rows), key=lambda index: objective[index]
        )
        if objective[entering] >= -tolerance:
            break

        candidates = [
            (row[-1] / row[entering], row_index)
            for row_index, row in enumerate(tableau[:-1])
            if row[entering] > tolerance
        ]
        if not candidates:
            raise RuntimeError("linear program is unbounded")

        _, pivot_row = min(candidates, key=lambda item: (item[0], item[1]))
        pivot = tableau[pivot_row][entering]
        tableau[pivot_row] = [value / pivot for value in tableau[pivot_row]]

        for row_index, row in enumerate(tableau):
            if row_index != pivot_row and abs(row[entering]) > tolerance:
                factor = row[entering]
                tableau[row_index] = [
                    value - factor * pivot_value
                    for value, pivot_value in zip(row, tableau[pivot_row])
                ]

    variables = [0.0] * columns
    for column in range(columns):
        one_rows = [
            row_index for row_index, row in enumerate(tableau[:-1])
            if abs(row[column] - 1.0) <= tolerance
            and all(abs(other[column]) <= tolerance
                    for other_index, other in enumerate(tableau[:-1])
                    if other_index != row_index)
        ]
        if one_rows:
            variables[column] = tableau[one_rows[0]][-1]

    return tableau[-1][-1], variables, tableau


if __name__ == "__main__":
    # maximise 3x + 2y subject to x + y <= 4, x <= 2, y <= 3
    value, variables, _ = simplex(
        [3, 2],
        [[1, 1], [1, 0], [0, 1]],
        [4, 2, 3],
    )
    print(f"Maximum: {value:g}; variables: {variables}")