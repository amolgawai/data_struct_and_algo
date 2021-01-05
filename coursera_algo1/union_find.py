"""Union Find implementations from the coursera course"""


class QuickFindUF:
    """Quick Find Union Find implementation

    Simple implementation suitable for small data set.

    The data is represented as an array of ids, index of array is a node
    The nodes with same ids are connected.
    Union can take a lot of time as it needs to find all the items with same
    ids by iterating through the entire array
    """

    def __init__(self, size):
        self.ids = list(i for i in range(size))

    def __str__(self):
        """Pretty print class"""
        return f"{self.ids}"

    def are_connected(self, id_1, id_2):
        """Retrurns Ttue if p and q are connected
        Keyword Arguments:
        id_1 -- first id
        id_2 -- second id
        """
        return self.ids[id_1] == self.ids[id_2]

    def union(self, id_1, id_2):
        """Connects (unioins) two ids
        Keyword Arguments:
        id_1 -- first id
        id_2 -- second id
        """

        if self.are_connected(id_1, id_2):
            return
        first = self.ids[id_1]
        second = self.ids[id_2]
        for indx, id_num in enumerate(self.ids):
            if id_num == first:
                self.ids[indx] = second


class QuickUnionUF:
    """Quick Union Union Find implementation

    The data is represented as an array of indices, indices represent nodes.
    Each node is also a leaf of a connection tree. Some nodes are root.
    The id of each node represents the root node.
    """

    def __init__(self, size):
        self.ids = list(i for i in range(size))

    def __str__(self):
        """Pretty print class"""
        return f"{self.ids}"

    def _root(self, i_d):
        """Find the root of id
        Keyword Arguments:
        id -- for which root is needed
        """

        while i_d != self.ids[i_d]:
            i_d = self.ids[i_d]

        return i_d

    def are_connected(self, id_1, id_2):
        """Retrurns Ttue if p and q are connected
        Keyword Arguments:
        id_1 -- first id
        id_2 -- second id
        """
        return self._root(id_1) == self._root(id_2)

    def union(self, id_1, id_2):
        """Connects (unioins) two ids
        Keyword Arguments:
        id_1 -- first id
        id_2 -- second id
        """

        first = self._root(id_1)
        second = self._root(id_2)
        self.ids[first] = second
