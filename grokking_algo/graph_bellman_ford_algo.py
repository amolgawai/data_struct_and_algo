"""Implements Bellman Ford Shortest Path algorithm.

Use this algorithm for a weighted graph with negative weight
"""
from collections import deque
from grokking_algo.graph_builder import (
    build_weighted_da_graph,
    get_vertices,
    get_path,
)


class GraphNegativeCycleError(Exception):
    "Negative Cycle found in the Graph"


def bellman_ford_algo(graph_dict, start_nd, dest_nd):
    """Run the Bellman Ford algorithm to find shortest path
    Keyword Arguments:
    graph_dict -- weighted graph in the form of a dictionary
    start_nd   -- starting node
    dest_nd     -- end node
    """
    infinity = float("inf")
    vertices = get_vertices(graph_dict)
    costs = {itm: infinity for itm in vertices}
    parents = {itm: None for itm in vertices}

    costs[start_nd] = 0
    for __ in range(len(vertices) - 1):
        for vertex, edges in graph_dict.items():
            for edge_nd, cost in edges.items():
                new_cost = costs[vertex] + cost
                if new_cost < costs[edge_nd]:
                    costs[edge_nd] = new_cost
                    parents[edge_nd] = vertex

    for vertex, edges in graph_dict.items():
        for edge_nd, cost in edges.items():
            if costs[vertex] + cost < costs[edge_nd]:
                error_msg = (
                    f"Negative cycle found between {vertex} & {edge_nd}"
                )
                raise GraphNegativeCycleError(error_msg)

    path_deque = get_path(parents, start_nd, dest_nd)
    return costs[dest_nd], path_deque


def main():  # pragma: no cover
    """Exploratory tests for the module."""
    graphs = (
        (("A", "B", 2), ("A", "C", -3), ("B", "D", -5), ("C", "D", 3)),
        (
            ("A", "B", 20),
            ("A", "C", 10),
            ("B", "D", 50),
            ("C", "D", 20),
            ("B", "E", 10),
            ("C", "E", 33),
            ("B", "E", 50),
            ("E", "D", -20),
            ("E", "F", 1),
            ("D", "F", -2),
        ),
    )

    for edges in graphs:
        graph = build_weighted_da_graph(edges)
        cost, path = bellman_ford_algo(
            graph, edges[0][0], edges[len(edges) - 1][1]
        )
        print(f"cost - {cost}")
        print("Path -", "->".join(path))

    neg_graphs = (
        (("A", "B", 1), ("B", "C", -1), ("C", "D", -1), ("D", "A", -1)),
        (
            ("A", "B", 1),
            ("B", "C", -5),
            ("C", "E", -5),
            ("E", "F", 1),
            ("E", "D", -5),
            ("D", "B", -5),
        ),
    )

    for edges in neg_graphs:
        graph = build_weighted_da_graph(edges)
        try:
            bellman_ford_algo(graph, edges[0][0], edges[len(edges) - 1][1])
        except GraphNegativeCycleError as err:
            print(err)


if __name__ == "__main__":
    main()
