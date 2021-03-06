"""Shortest path finding of a weighted graph using Dijkstra's Algorithm."""
from collections import deque
from grokking_algo.graph_builder import (
    build_weighted_da_graph,
    get_vertices,
    get_path,
)


def dijkstras_algo(graph_dict, start_nd, dest_nd):
    """Run the Dijkstra's Algorithm.

    Run Dijkstra's algorithm on the weighted graph dict and return shortest
    path.
    """
    infinity = float("inf")
    vertices = get_vertices(graph_dict)
    costs = {itm: infinity for itm in vertices if itm != start_nd}
    parents = {itm: None for itm in vertices if itm != start_nd}
    processed = list()

    costs[start_nd] = 0
    a_node = start_nd
    while a_node:
        cost = costs[a_node]
        neigbhours = graph_dict[a_node]
        for nb, nb_cost in neigbhours.items():
            new_cost = cost + nb_cost
            if costs[nb] > new_cost:
                costs[nb] = new_cost
                parents[nb] = a_node

        if a_node == dest_nd:
            break

        processed.append(a_node)
        a_node = min(
            costs,
            key=lambda node: costs[node]
            if node not in processed
            else infinity,
        )

    path_deque = get_path(parents, start_nd, dest_nd)
    return costs[dest_nd], path_deque


def main():  # pragma: no cover
    """Manually testing the algorithm."""
    graphs = (
        (
            ("start", "a", 6),
            ("start", "b", 2),
            ("a", "fin", 1),
            ("b", "a", 3),
            ("b", "fin", 5),
        ),
        (
            ("start", "a", 5),
            ("start", "b", 2),
            ("a", "c", 4),
            ("a", "d", 2),
            ("b", "a", 8),
            ("b", "d", 7),
            ("c", "d", 6),
            ("c", "d", 6),
            ("c", "fin", 3),
            ("d", "fin", 1),
        ),
        (
            ("a", "b", 7),
            ("a", "c", 9),
            ("a", "f", 14),
            ("b", "c", 10),
            ("b", "d", 15),
            ("c", "d", 11),
            ("c", "f", 2),
            ("d", "e", 6),
            ("e", "f", 9),
        ),
    )

    for edges in graphs:
        graph = build_weighted_da_graph(edges)
        cost, path = dijkstras_algo(
            graph, edges[0][0], edges[len(edges) - 1][1]
        )
        print(f"cost - {cost}")
        print("Path -", "->".join(path))


if __name__ == "__main__":
    main()
