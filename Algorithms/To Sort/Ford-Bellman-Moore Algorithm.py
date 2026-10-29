"""Ford–Bellman–Moore (Bellman–Ford) shortest-path algorithm."""


def ford_bellman_moore(graph, start):
    """Return shortest distances and predecessors from ``start``.

    ``graph`` is a mapping of vertices to iterables of ``(neighbour, weight)``
    pairs.  Vertices with no outgoing edges may be omitted or have an empty
    iterable.  A ``ValueError`` is raised if a negative-weight cycle reachable
    from ``start`` exists.
    """
    vertices = set(graph)
    for edges in graph.values():
        vertices.update(neighbour for neighbour, _ in edges)

    if start not in vertices:
        raise ValueError("start vertex is not in the graph")

    infinity = float("inf")
    distance = {vertex: infinity for vertex in vertices}
    predecessor = {vertex: None for vertex in vertices}
    distance[start] = 0

    edges = [
        (vertex, neighbour, weight)
        for vertex, outgoing in graph.items()
        for neighbour, weight in outgoing
    ]

    for _ in range(len(vertices) - 1):
        changed = False
        for vertex, neighbour, weight in edges:
            if distance[vertex] != infinity and distance[vertex] + weight < distance[neighbour]:
                distance[neighbour] = distance[vertex] + weight
                predecessor[neighbour] = vertex
                changed = True
        if not changed:
            break

    if any(
        distance[vertex] != infinity
        and distance[vertex] + weight < distance[neighbour]
        for vertex, neighbour, weight in edges
    ):
        raise ValueError("graph contains a reachable negative-weight cycle")

    return distance, predecessor


if __name__ == "__main__":
    graph = {
        "A": [("B", 4), ("C", 2)],
        "B": [("C", -1), ("D", 2)],
        "C": [("D", 3)],
        "D": [],
    }
    distances, predecessors = ford_bellman_moore(graph, "A")
    print(distances)
