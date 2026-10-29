"""Solve a system of linear equations with the Gauss-Seidel method."""


def gauss_seidel(coefficients, constants, tolerance=1e-10,
				 max_iterations=1000, initial_guess=None):
	"""Return x for coefficients @ x = constants."""
	size = len(constants)
	if (size == 0 or len(coefficients) != size or
			any(len(row) != size for row in coefficients)):
		raise ValueError("coefficients must be a non-empty square matrix")
	if any(coefficients[i][i] == 0 for i in range(size)):
		raise ValueError("diagonal coefficients cannot be zero")
	if tolerance <= 0 or max_iterations <= 0:
		raise ValueError("tolerance and max_iterations must be positive")

	values = ([0.0] * size if initial_guess is None
			  else [float(value) for value in initial_guess])
	if len(values) != size:
		raise ValueError("initial_guess must match the system size")

	for _ in range(max_iterations):
		previous = values.copy()
		for row in range(size):
			other_terms = sum(coefficients[row][column] * values[column]
							  for column in range(size) if column != row)
			values[row] = (constants[row] - other_terms) / coefficients[row][row]

		if max(abs(values[i] - previous[i]) for i in range(size)) < tolerance:
			return values

	raise ValueError("Gauss-Seidel method did not converge")


if __name__ == "__main__":
	matrix = [[4, 1, 1], [2, 7, 1], [1, -3, 12]]
	constants = [7, -21, 15]
	print(gauss_seidel(matrix, constants))
