"""Breadth first search with a graph represented by dictionary."""
from collections import deque


def bfs(graph_dict, start, key_func):
    """ Performs Breadth First Search on the graph stopping at the criterion.

    Keyword Arguments:
    graph_dict: -- graph represented by a dictionary
    start: -- search start
    key: -- predicate to stop at as a search end criterion
    """
    search_queue = deque()
    search_queue += graph_dict[start]
    while search_queue:
        node = search_queue.popleft()
        if key_func(node):
            return node
        search_queue += graph_dict[node]

    return None


def main():  # pragma: no cover
    "Manually test the algorithm."
    graph = {}
    graph["you"] = ["alice", "bob", "claire"]
    graph["bob"] = ["anuj", "peggy"]
    graph["alice"] = ["peggy"]
    graph["claire"] = ["thom", "jonny"]
    graph["anuj"] = []
    graph["peggy"] = []
    graph["thom"] = []
    graph["jonny"] = []

    print(bfs(graph, "you", lambda x: x.endswith('m')))
    print(bfs(graph, "you", lambda x: x.endswith('y')))


if __name__ == "__main__":
    main()
