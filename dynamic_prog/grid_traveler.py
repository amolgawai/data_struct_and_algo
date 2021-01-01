"""find out number of ways to traverse a grid
condition - start from top left and move either right or down
"""
from memoization import cached


def grid_travel_rec_brt_frc(rows, colmns):
    """Brute force calculation of number of ways to travel in a grid
    Keyword Arguments:
    rows   -- number of rows
    colmns -- number of columns
    """

    if rows == 0 or colmns == 0:
        return 0

    if rows == colmns == 1:
        return 1

    return grid_travel_rec_brt_frc(rows - 1, colmns) + grid_travel_rec_brt_frc(
        rows, colmns - 1
    )


@cached(order_independent=True)
def grid_travel_rec_memzd(rows, colmns):
    """Memoized calculation of number of ways to travel in a grid
    Keyword Arguments:
    rows   -- number of rows
    colmns -- number of columns
    """

    if rows == 0 or colmns == 0:
        return 0

    if rows == colmns == 1:
        return 1

    return grid_travel_rec_memzd(rows - 1, colmns) + grid_travel_rec_memzd(
        rows, colmns - 1
    )


def grid_travel_tab(rows, colmns):
    """Grid travel with iterative and tabulation technique
    Keyword Arguments:
    rows   -- number of rows
    colmns -- number of columns
    """

    if rows == 0 or colmns == 0:
        return 0

    if rows == colmns == 1:
        return 1

    # grid = [[0] * (colmns + 1)] * (rows + 1) - same row copied rows + 1 times
    grid = [[0] * (colmns + 1) for _ in range(rows + 1)]
    grid[1][1] = 1
    for row in range(rows + 1):
        for clmn in range(colmns + 1):
            cur = grid[row][clmn]
            if clmn + 1 <= colmns:
                grid[row][clmn + 1] += cur
            if row + 1 <= rows:
                grid[row + 1][clmn] += cur

    return grid[rows][colmns]


def run_algo(grid_size_lst, algo_func, msg):
    """run a specific algorithm given the gid size and algorithm function
    Keyword Arguments:
    grid_size_lst -- List of grid size tuple, e.g. [(2, 3), (5, 5)]
    algo_func -- function to run
    msg -- message to display
    """

    print(msg)
    for grid in grid_size_lst:
        print(f"grid {grid}: {algo_func(grid[0], grid[1])}")

    print("-----------")


def main():
    """The main function"""
    grids = [(0, 1), (1, 1), (2, 3), (5, 5), (10, 10), (18, 18), (50, 100)]

    msg1 = "Brute Force grid traversal"
    run_algo(
        filter(lambda tpl: tpl[0] <= 8 and tpl[1] <= 8, grids),
        grid_travel_rec_brt_frc,
        msg1,
    )

    msg2 = "Memoized grid traversal"
    run_algo(grids, grid_travel_rec_memzd, msg2)

    msg3 = "Tabulated grid traversal"
    run_algo(grids, grid_travel_tab, msg3)


if __name__ == "__main__":
    main()
