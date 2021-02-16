"""Tests Bellman Ford Shortes Path Algorithm for negative weighted graph."""
import pytest
from grokking_algo.graph_builder import build_weighted_da_graph
from grokking_algo.graph_bellman_ford_algo import (
    bellman_ford_algo,
    GraphNegativeCycleError,
)


def test_bellman_ford_positive():
    """Test the positive case of Bellman Ford Algorithm"""
    graph = build_weighted_da_graph(
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
        )
    )
    cost_expected = 21
    path_expected = ("A", "C", "E", "D", "F")
    cost, path = bellman_ford_algo(graph, "A", "F")
    assert cost == cost_expected
    assert tuple(path) == path_expected


def test_bellman_ford_exception():
    """Test for negative cycle exception"""
    grah_negative = build_weighted_da_graph(
        (
            ("A", "B", 1),
            ("B", "C", -5),
            ("C", "E", -5),
            ("E", "F", 1),
            ("E", "D", -5),
            ("D", "B", -5),
        )
    )
    with pytest.raises(GraphNegativeCycleError) as excinfo:
        bellman_ford_algo(grah_negative, "A", "F")

    assert "Negative cycle found" in str(excinfo.value)
