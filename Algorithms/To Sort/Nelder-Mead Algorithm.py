"""Nelder–Mead simplex optimization.

This derivative-free method minimizes a scalar function over a continuous
parameter space.  It is useful when derivatives are unavailable or expensive.
"""

from math import fsum, isfinite


def nelder_mead(
	function,
	start,
	step=1.0,
	tolerance=1e-8,
	max_iterations=10_000,
	reflection=1.0,
	expansion=2.0,
	contraction=0.5,
	shrink=0.5,
):
	"""Return ``(best_point, best_value, iterations)`` for ``function``.

	``start`` is an iterable containing the initial point.  The function is
	minimized without requiring gradients.
	"""
	point = [float(value) for value in start]
	dimensions = len(point)
	if dimensions == 0:
		raise ValueError("start must contain at least one value")
	if step <= 0 or tolerance <= 0 or max_iterations < 1:
		raise ValueError("step, tolerance, and max_iterations must be positive")

	simplex = [point]
	for index in range(dimensions):
		vertex = point.copy()
		vertex[index] += step
		simplex.append(vertex)

	def evaluate(vertex):
		value = float(function(vertex))
		if not isfinite(value):
			raise ValueError("function must return a finite number")
		return value

	values = [evaluate(vertex) for vertex in simplex]

	for iteration in range(1, max_iterations + 1):
		order = sorted(range(dimensions + 1), key=values.__getitem__)
		simplex = [simplex[index] for index in order]
		values = [values[index] for index in order]

		spread = values[-1] - values[0]
		size = max(
			max(abs(a - b) for a, b in zip(vertex, simplex[0]))
			for vertex in simplex[1:]
		)
		if spread <= tolerance and size <= tolerance:
			return simplex[0], values[0], iteration - 1

		centroid = [
			fsum(simplex[index][coordinate] for index in range(dimensions))
			/ dimensions
			for coordinate in range(dimensions)
		]

		def combination(first, second, factor):
			return [a + factor * (a - b) for a, b in zip(first, second)]

		reflected = combination(centroid, simplex[-1], reflection)
		reflected_value = evaluate(reflected)

		if values[0] <= reflected_value < values[-2]:
			simplex[-1], values[-1] = reflected, reflected_value
		elif reflected_value < values[0]:
			expanded = combination(centroid, simplex[-1], expansion)
			expanded_value = evaluate(expanded)
			simplex[-1], values[-1] = (
				(expanded, expanded_value)
				if expanded_value < reflected_value
				else (reflected, reflected_value)
			)
		else:
			contracted = combination(
				centroid,
				simplex[-1],
				contraction if reflected_value < values[-1] else -contraction,
			)
			contracted_value = evaluate(contracted)
			if contracted_value < min(values[-1], reflected_value):
				simplex[-1], values[-1] = contracted, contracted_value
			else:
				best = simplex[0]
				for index in range(1, dimensions + 1):
					simplex[index] = [
						best_coordinate
						+ shrink * (coordinate - best_coordinate)
						for coordinate, best_coordinate in zip(
							simplex[index], best
						)
					]
					values[index] = evaluate(simplex[index])

	order = min(range(dimensions + 1), key=values.__getitem__)
	return simplex[order], values[order], max_iterations


if __name__ == "__main__":
	def sphere(point):
		return sum(value * value for value in point)


	minimum, value, iterations = nelder_mead(sphere, [3, -4])
	print(f"minimum={minimum}, value={value:.3g}, iterations={iterations}")
