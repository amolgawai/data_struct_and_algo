"""Utility module that builds various graph data structures"""
from collections import defaultdict, deque


def build_weighted_da_graph(edges):
    """Build a graph dictionary from the edges."""
    graph = defaultdict(lambda: defaultdict(dict))

    for v1, v2, wt in edges:
        graph[v1][v2] = wt

    return graph


def get_vertices(graph_dict):
    """Get vertices from the graph dictionary.

    Keyword Arguments:
    graph_dict -- graph represented as a dictionary
    Returns:
    map -- map of vertices
    """
    vertices = {
        vertx
        for vert_dict in graph_dict.values()
        for vertx in vert_dict.keys()
    } | set(graph_dict.keys())

    return vertices


def get_path(nd_parent_dict, start_nd, dest_nd):
    """Get the path between start node and destination node.
    Keyword Arguments:
    nd_parent_dict -- dictionary in the form Node:Parent
    start_nd       -- Start node of the required path
    dest_nd        -- Destination node of the required path
    Returns:
    path in for of deque
    """
    graph_path = deque((dest_nd,))
    path_nd = dest_nd
    while path_nd != start_nd:
        path_nd = nd_parent_dict[path_nd]
        graph_path.appendleft(path_nd)

    return graph_path
