"""Utility module that builds various graph data structures"""
from collections import defaultdict


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
