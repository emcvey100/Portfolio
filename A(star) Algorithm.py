"""A* path-finding for a two-dimensional grid.

Cells containing a truthy value are treated as blocked.  The returned path
includes both ``start`` and ``goal``; an empty list means no path exists.
"""

from heapq import heappop, heappush
from itertools import count


def a_star(grid, start, goal):
    """Return the shortest path through ``grid`` from ``start`` to ``goal``.

    Coordinates are ``(row, column)``.  Movement is allowed horizontally and
    vertically, and every move has a cost of one.
    """
    rows = len(grid)
    if not rows or any(len(row) != len(grid[0]) for row in grid):
        return []

    columns = len(grid[0])

    def valid(cell):
        row, column = cell
        return (
            0 <= row < rows
            and 0 <= column < columns
            and not grid[row][column]
        )

    if not valid(start) or not valid(goal):
        return []

    def heuristic(cell):
        return abs(cell[0] - goal[0]) + abs(cell[1] - goal[1])

    frontier = []
    sequence = count()
    heappush(frontier, (heuristic(start), next(sequence), start))
    came_from = {start: None}
    cost_so_far = {start: 0}

    while frontier:
        _, _, current = heappop(frontier)
        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = came_from[current]
            return path[::-1]

        row, column = current
        for neighbor in (
            (row - 1, column),
            (row + 1, column),
            (row, column - 1),
            (row, column + 1),
        ):
            if not valid(neighbor):
                continue
            new_cost = cost_so_far[current] + 1
            if new_cost < cost_so_far.get(neighbor, float("inf")):
                cost_so_far[neighbor] = new_cost
                came_from[neighbor] = current
                priority = new_cost + heuristic(neighbor)
                heappush(frontier, (priority, next(sequence), neighbor))

    return []


if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 0],
    ]
    print(a_star(grid, (0, 0), (2, 3)))