"""Test Dijkastra's Algorithm.

Simple tests for now until get the test data
"""
from grokking_algo.graph_dijkstras_algo import dijkstras_algo, build_graph


def test_dijkstras_algo():
    """Test the Dijkstra's algorithm."""
    graph = build_graph(
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
        )
    )

    expected_ae = (("a", "c", "d", "e"), 26)
    cost, path = dijkstras_algo(graph, "a", "e")
    assert tuple(path) == expected_ae[0]
    assert cost == expected_ae[1]

    expected_af = (("a", "c", "f"), 11)
    cost, path = dijkstras_algo(graph, "a", "f")
    assert tuple(path) == expected_af[0]
    assert cost == expected_af[1]
