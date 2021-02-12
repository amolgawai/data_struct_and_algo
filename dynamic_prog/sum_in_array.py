""" Vaiety of functions that are related to finding sum of a target
number from a given array
"""
from memoization import cached


@cached
def can_sum_mem(target_sum, num_tpl):
    """Finds if the sum can be constructed from numbers in the array
    Keyword Arguments:
    target_sum -- the taget sum that needs to be constructed
    num_lst    -- the tuples describing array of numbers
    """

    if target_sum == 0:
        return True
    if target_sum < 0:
        return False

    for a_num in num_tpl:
        if can_sum_mem(target_sum - a_num, num_tpl):
            return True

    return False


def can_sum_tabl(target_sum, num_tpl):
    """ Tabulation implementation of can_sum"""

    tbl = [False] * (target_sum + 1)
    tbl[0] = True

    for indx, a_tbl in enumerate(tbl):
        if a_tbl:
            for a_num in num_tpl:
                if indx + a_num <= target_sum:
                    tbl[indx + a_num] = True

    return tbl[-1]


@cached
def how_sum_mem(target_sum, num_tpl):
    """returns a sub array of num_tpl sum of which equals target_sum
    returns a None in case no sum can be found
    """

    if target_sum == 0:
        return []
    if target_sum < 0:
        return None

    for a_num in num_tpl:
        res = how_sum_mem(target_sum - a_num, num_tpl)
        if res is not None:
            sum_combo = res + [a_num]
            return sum_combo

    return None


def how_sum_tabl(target_sum, num_tpl):
    """Tabulation implementation of how sum"""

    tbl = [None] * (target_sum + 1)
    tbl[0] = []

    for indx in range(target_sum + 1):
        a_tbl = tbl[indx]
        if a_tbl is not None:
            for a_num in num_tpl:
                if indx + a_num <= target_sum:
                    tbl[indx + a_num] = a_tbl + [a_num]

    return tbl[-1]


@cached
def best_sum_mem(target_sum, num_tpl):
    """returns a smallest sub array of num_tpl sum of which equals target_sum
    returns a None array in case no sum can be found
    """

    if target_sum == 0:
        return []
    if target_sum < 0:
        return None

    shortest_combo = None
    for a_num in num_tpl:
        res = best_sum_mem(target_sum - a_num, num_tpl)
        if res is not None:
            sum_combo = res + [a_num]
            if not shortest_combo or len(sum_combo) < len(shortest_combo):
                shortest_combo = list(sum_combo)

    return shortest_combo


def best_sum_tabl(target_sum, num_tpl):
    """Tabulation implementation of how sum"""

    tbl = [None] * (target_sum + 1)
    tbl[0] = []

    for indx in range(target_sum + 1):
        a_tbl = tbl[indx]
        if a_tbl is not None:
            for a_num in num_tpl:
                if indx + a_num <= target_sum:
                    sum_combo = a_tbl + [a_num]
                    cur_combo = tbl[indx + a_num]
                    if not cur_combo or len(sum_combo) < len(cur_combo):
                        tbl[indx + a_num] = list(sum_combo)

    return tbl[-1]


def run_algo(input_tpl_lst, algo_func, msg):  # pragma: no cover
    """Runs an algorithm and prints output"""

    print(msg)
    for input_tpl in input_tpl_lst:
        print(algo_func(input_tpl[0], input_tpl[1]))

    print("=================")


def main():  # pragma: no cover
    """Manual testing"""

    inputs = ((7, (3, 4, 5, 7)), (7, (7, 3, 4, 5)), (300, (7, 14)))

    run_algo(inputs, can_sum_mem, "Memoized can sum")
    run_algo(inputs, can_sum_tabl, "Tabulation can sum")
    run_algo(inputs, how_sum_mem, "Memoized how sum")
    run_algo(inputs, how_sum_tabl, "Tabulation how sum")
    run_algo(inputs, best_sum_mem, "Memoized best sum")
    run_algo(inputs, best_sum_tabl, "Tabulation best sum")


if __name__ == "__main__":
    main()
