"""Tests for breadth first search algorithm."""
import pytest
from grokking_algo.graph_bfs import bfs


@pytest.fixture(autouse=True)
def graph_dict():
    """Prepares the graph for testing."""
    graph = {}
    graph["you"] = ["alice", "bob", "claire"]
    graph["bob"] = ["anuj", "peggy"]
    graph["alice"] = ["peggy"]
    graph["claire"] = ["thom", "jonny"]
    graph["anuj"] = []
    graph["peggy"] = []
    graph["thom"] = []
    graph["jonny"] = []
    return graph


def test_positive_bfs(graph_dict):
    """Tests the positive case for bfs algorithm."""
    assert bfs(graph_dict, "you", lambda x: x.endswith("m")) == "thom"
    assert bfs(graph_dict, "you", lambda x: x.endswith("y")) == "peggy"
    assert bfs(graph_dict, "bob", lambda x: x.endswith("gy")) == "peggy"


def test_negative_bfs(graph_dict):
    """Tests the negative case for bfs algorithm"""
    assert bfs(graph_dict, "you", lambda x: x.endswith("z")) is None
