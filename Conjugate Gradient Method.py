"""Solve a symmetric positive-definite system with the conjugate gradient method."""

import numpy as np


def conjugate_gradient(A, b, x0=None, tol=1e-10, max_iter=None):
	"""Return ``x`` satisfying ``A @ x = b``.

	``A`` must be symmetric positive-definite.  The iteration stops when the
	Euclidean norm of the residual is at most ``tol``.
	"""
	A = np.asarray(A, dtype=float)
	b = np.asarray(b, dtype=float)

	if A.ndim != 2 or A.shape[0] != A.shape[1]:
		raise ValueError("A must be a square matrix")
	if b.ndim != 1 or b.size != A.shape[0]:
		raise ValueError("b must be a vector with one entry per row of A")
	if tol < 0:
		raise ValueError("tol must be non-negative")

	n = b.size
	x = np.zeros(n) if x0 is None else np.asarray(x0, dtype=float).copy()
	if x.shape != b.shape:
		raise ValueError("x0 must have the same shape as b")
	if max_iter is None:
		max_iter = n
	if max_iter < 0:
		raise ValueError("max_iter must be non-negative")

	residual = b - A @ x
	direction = residual.copy()
	residual_squared = np.dot(residual, residual)

	for _ in range(max_iter):
		if np.sqrt(residual_squared) <= tol:
			break
		Adirection = A @ direction
		denominator = np.dot(direction, Adirection)
		if denominator <= 0:
			raise ValueError("A must be positive-definite")

		step = residual_squared / denominator
		x += step * direction
		new_residual = residual - step * Adirection
		new_residual_squared = np.dot(new_residual, new_residual)
		if np.sqrt(new_residual_squared) <= tol:
			break

		direction = new_residual + (new_residual_squared / residual_squared) * direction
		residual = new_residual
		residual_squared = new_residual_squared

	return x


if __name__ == "__main__":
	matrix = np.array([[4.0, 1.0], [1.0, 3.0]])
	vector = np.array([1.0, 2.0])
	print(conjugate_gradient(matrix, vector))
