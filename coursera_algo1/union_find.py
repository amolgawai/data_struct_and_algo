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
        for id_num in self.ids:
            if id_num == first:
                self.ids[id_num] = second


def main():
    """Main function for testing"""
    qf_uf = QuickFindUF(10)
    print(qf_uf)
    print(qf_uf.are_connected(0, 5))
    qf_uf.union(0, 5)
    print(qf_uf.are_connected(0, 5))
    print(qf_uf)


if __name__ == "__main__":
    main()
