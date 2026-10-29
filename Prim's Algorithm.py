"""Prim's algorithm for finding a minimum spanning tree."""

from heapq import heappop, heappush


def prims_algorithm(graph, start=None):
    """Return the minimum spanning tree and its total weight.

    ``graph`` is an adjacency dictionary whose values are ``(neighbour,
    weight)`` pairs.  The graph must be connected and undirected.
    """
    if not graph:
        return [], 0

    start = next(iter(graph)) if start is None else start
    if start not in graph:
        raise ValueError("start vertex is not in the graph")

    visited = {start}
    edges = []
    for neighbour, weight in graph[start]:
        heappush(edges, (weight, start, neighbour))

    minimum_spanning_tree = []
    total_weight = 0

    while edges and len(visited) < len(graph):
        weight, source, destination = heappop(edges)
        if destination in visited:
            continue

        visited.add(destination)
        minimum_spanning_tree.append((source, destination, weight))
        total_weight += weight

        for neighbour, edge_weight in graph[destination]:
            if neighbour not in visited:
                heappush(edges, (edge_weight, destination, neighbour))

    if len(visited) != len(graph):
        raise ValueError("graph must be connected")

    return minimum_spanning_tree, total_weight


if __name__ == "__main__":
    graph = {
        "A": [("B", 4), ("C", 2)],
        "B": [("A", 4), ("C", 1), ("D", 5)],
        "C": [("A", 2), ("B", 1), ("D", 8)],
        "D": [("B", 5), ("C", 8)],
    }

    tree, weight = prims_algorithm(graph)
    print("Minimum spanning tree:", tree)
    print("Total weight:", weight)