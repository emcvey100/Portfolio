"""A* pathfinding for a rectangular grid."""

from heapq import heappop, heappush


def _manhattan_distance(first, second):
	"""Return the Manhattan distance between two (row, column) cells."""
	return abs(first[0] - second[0]) + abs(first[1] - second[1])


def a_star(grid, start, goal):
	"""Return the shortest path from ``start`` to ``goal``.

	``grid`` is a sequence of rows where truthy cells are blocked. Movement
	is allowed up, down, left, and right. The path includes both endpoints;
	``None`` is returned when no path exists.
	"""
	if not grid or not all(grid) or not all(grid[0]):
		return None

	rows, columns = len(grid), len(grid[0])

	def is_open(cell):
		row, column = cell
		return (
			0 <= row < rows
			and 0 <= column < columns
			and not grid[row][column]
		)

	if not is_open(start) or not is_open(goal):
		return None

	frontier = []
	heappush(frontier, (_manhattan_distance(start, goal), 0, start))
	came_from = {start: None}
	cost_so_far = {start: 0}

	while frontier:
		_, cost, current = heappop(frontier)
		if cost != cost_so_far[current]:
			continue

		if current == goal:
			path = []
			while current is not None:
				path.append(current)
				current = came_from[current]
			return path[::-1]

		row, column = current
		neighbours = (
			(row - 1, column),
			(row + 1, column),
			(row, column - 1),
			(row, column + 1),
		)
		for neighbour in neighbours:
			if not is_open(neighbour):
				continue
			new_cost = cost + 1
			if new_cost < cost_so_far.get(neighbour, float("inf")):
				cost_so_far[neighbour] = new_cost
				priority = new_cost + _manhattan_distance(neighbour, goal)
				heappush(frontier, (priority, new_cost, neighbour))
				came_from[neighbour] = current

	return None


if __name__ == "__main__":
	example_grid = [
		[False, False, False, False],
		[False, True, True, False],
		[False, False, False, False],
	]
	print(a_star(example_grid, (0, 0), (2, 3)))
