"""Union Find implementations from the coursera course"""


class QuickFindUF:
    """Quick Find Union Find implementation"""

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
        first = self.ids[id_1]
        second = self.ids[id_2]
        for indx, id_num in enumerate(self.ids):
            if id_num == first:
                self.ids[indx] = second
