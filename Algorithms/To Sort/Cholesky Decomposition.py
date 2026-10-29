"""Cholesky decomposition.

For a symmetric positive-definite matrix A, computes the lower-triangular
matrix L such that A = L @ L.T.
"""

from math import sqrt


def cholesky_decomposition(matrix):
    """Return the lower-triangular Cholesky factor of ``matrix``.

    Raises:
        ValueError: If the matrix is not square, symmetric, or positive
            definite.
    """
    n = len(matrix)
    if n == 0 or any(len(row) != n for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    if any(matrix[i][j] != matrix[j][i] for i in range(n) for j in range(i)):
        raise ValueError("matrix must be symmetric")

    lower = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1):
            remainder = matrix[i][j] - sum(
                lower[i][k] * lower[j][k] for k in range(j)
            )

            if i == j:
                if remainder <= 0:
                    raise ValueError("matrix must be positive definite")
                lower[i][j] = sqrt(remainder)
            else:
                lower[i][j] = remainder / lower[j][j]

    return lower


if __name__ == "__main__":
    matrix = [[4, 12, -16], [12, 37, -43], [-16, -43, 98]]
    print(cholesky_decomposition(matrix))
