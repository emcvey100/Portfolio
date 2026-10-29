from collections import deque


def breadth_first_search(graph, start, target):
    """Return the shortest path from start to target, or None if not found."""
    queue = deque([start])
    visited = {start}
    previous = {start: None}

    while queue:
        current = queue.popleft()

        if current == target:
            path = []
            while current is not None:
                path.append(current)
                current = previous[current]
            return path[::-1]

        for neighbour in graph.get(current, []):
            if neighbour not in visited:
                visited.add(neighbour)
                previous[neighbour] = current
                queue.append(neighbour)

    return None


if __name__ == "__main__":
    graph = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F"],
        "D": [],
        "E": ["F"],
        "F": [],
    }

    print(breadth_first_search(graph, "A", "F"))
