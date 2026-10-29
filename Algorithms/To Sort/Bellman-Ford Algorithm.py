"""Bellman-Ford shortest-path algorithm."""


def bellman_ford(vertices, edges, source):
    """Return shortest distances and predecessors from ``source``.

    ``vertices`` is an iterable of vertex labels and ``edges`` contains
    ``(start, end, weight)`` tuples.  Raises ``ValueError`` when a reachable
    negative-weight cycle exists.
    """
    vertices = list(vertices)
    if source not in vertices:
        raise ValueError("source must be in vertices")

    distances = {vertex: float("inf") for vertex in vertices}
    predecessors = {vertex: None for vertex in vertices}
    distances[source] = 0

    for _ in range(len(vertices) - 1):
        changed = False
        for start, end, weight in edges:
            if start not in distances or end not in distances:
                raise ValueError("edges contain an unknown vertex")
            if distances[start] != float("inf") and distances[start] + weight < distances[end]:
                distances[end] = distances[start] + weight
                predecessors[end] = start
                changed = True
        if not changed:
            break

    for start, end, weight in edges:
        if distances[start] != float("inf") and distances[start] + weight < distances[end]:
            raise ValueError("graph contains a reachable negative-weight cycle")

    return distances, predecessors


if __name__ == "__main__":
    graph_vertices = ("A", "B", "C", "D")
    graph_edges = (
        ("A", "B", 4),
        ("A", "C", 5),
        ("B", "C", -2),
        ("C", "D", 3),
    )
    distances, _ = bellman_ford(graph_vertices, graph_edges, "A")
    print(distances)
