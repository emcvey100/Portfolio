"""Fast Marching Method for shortest arrival times on a 2-D grid."""

from heapq import heappop, heappush
from math import inf, sqrt


def fast_marching(speed, sources, spacing=(1.0, 1.0)):
	"""Compute arrival times for a grid of positive propagation speeds.

	``sources`` contains ``(row, column)`` coordinates. Non-positive speed
	cells are obstacles and remain ``float('inf')``.
	"""
	if not speed or not speed[0]:
		return []
	rows, cols = len(speed), len(speed[0])
	if any(len(row) != cols for row in speed):
		raise ValueError("speed must be rectangular")
	if spacing[0] <= 0 or spacing[1] <= 0:
		raise ValueError("spacing must be positive")

	time = [[inf] * cols for _ in range(rows)]
	accepted = [[False] * cols for _ in range(rows)]
	queue = []
	for row, col in sources:
		if not (0 <= row < rows and 0 <= col < cols):
			raise ValueError("source is outside the grid")
		if speed[row][col] <= 0:
			raise ValueError("source must be traversable")
		time[row][col] = 0.0
		heappush(queue, (0.0, row, col))

	def update(row, col):
		neighbours = []
		if row > 0 and accepted[row - 1][col]:
			neighbours.append((time[row - 1][col], spacing[0]))
		if row + 1 < rows and accepted[row + 1][col]:
			neighbours.append((time[row + 1][col], spacing[0]))
		if col > 0 and accepted[row][col - 1]:
			neighbours.append((time[row][col - 1], spacing[1]))
		if col + 1 < cols and accepted[row][col + 1]:
			neighbours.append((time[row][col + 1], spacing[1]))
		if not neighbours:
			return inf
		neighbours.sort()
		first, h = neighbours[0]
		reciprocal_speed = 1.0 / speed[row][col]
		result = first + h * reciprocal_speed
		if len(neighbours) > 1:
			second, k = neighbours[1]
			a = h ** -2 + k ** -2
			b = -2 * (first / h ** 2 + second / k ** 2)
			c = first ** 2 / h ** 2 + second ** 2 / k ** 2 - reciprocal_speed ** 2
			root = (-b + sqrt(max(0.0, b * b - 4 * a * c))) / (2 * a)
			if root >= second:
				result = root
		return result

	while queue:
		value, row, col = heappop(queue)
		if accepted[row][col] or value != time[row][col]:
			continue
		accepted[row][col] = True
		for nr, nc in ((row - 1, col), (row + 1, col),
					   (row, col - 1), (row, col + 1)):
			if (0 <= nr < rows and 0 <= nc < cols and
					speed[nr][nc] > 0 and not accepted[nr][nc]):
				candidate = update(nr, nc)
				if candidate < time[nr][nc]:
					time[nr][nc] = candidate
					heappush(queue, (candidate, nr, nc))
	return time


if __name__ == "__main__":
	grid = [[1.0] * 25 for _ in range(25)]
	print(fast_marching(grid, [(12, 12)])[0][0])
