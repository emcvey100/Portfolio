"""Ramer-Douglas-Peucker polyline simplification algorithm."""

from math import hypot
from typing import Sequence, TypeAlias

Point: TypeAlias = Sequence[float]


def _perpendicular_distance(point: Point, start: Point, end: Point) -> float:
	"""Return the shortest distance from *point* to the segment start-end."""
	dx = end[0] - start[0]
	dy = end[1] - start[1]

	if dx == 0 and dy == 0:
		return hypot(point[0] - start[0], point[1] - start[1])

	parameter = (
		(point[0] - start[0]) * dx + (point[1] - start[1]) * dy
	) / (dx * dx + dy * dy)
	parameter = max(0.0, min(1.0, parameter))
	projection = (start[0] + parameter * dx, start[1] + parameter * dy)
	return hypot(point[0] - projection[0], point[1] - projection[1])


def simplify(points: Sequence[Point], epsilon: float) -> list[Point]:
	"""Simplify a 2-D polyline using the Ramer-Douglas-Peucker algorithm.

	``epsilon`` is the maximum permitted distance from the simplified line.
	The input is not modified; the original point objects are returned.
	"""
	if epsilon < 0:
		raise ValueError("epsilon must be non-negative")
	if len(points) <= 2:
		return list(points)

	greatest_distance = epsilon
	split_index = -1
	for index in range(1, len(points) - 1):
		distance = _perpendicular_distance(points[index], points[0], points[-1])
		if distance > greatest_distance:
			greatest_distance = distance
			split_index = index

	if split_index == -1:
		return [points[0], points[-1]]

	left = simplify(points[: split_index + 1], epsilon)
	right = simplify(points[split_index:], epsilon)
	return left[:-1] + right


ramer_douglas_peucker = simplify
