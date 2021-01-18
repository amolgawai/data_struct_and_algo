#!/usr/bin/env python
"""Dynamic programming for constructing a string by taking words from an aray"""
from memoization import cached


@cached
def can_construct_mem(target_str, str_array):
    """Tests weather a string can be constructed out of words from an array
    memoized solution
    """

    if target_str == "":
        return True

    for a_str in str_array:
        if target_str.startswith(a_str):
            if can_construct_mem(target_str.split(a_str, 1)[1], str_array):
                return True

    return False


def can_construct_tabl(target_str, str_array):
    """Tabulation algorithm for can costruct"""

    tbl = [False] * (len(target_str) + 1)
    tbl[0] = True

    for indx, a_tbl in enumerate(tbl):
        if a_tbl:
            for a_str in str_array:
                if target_str[indx:].startswith(a_str):
                    tbl[indx + len(a_str)] = True

    return tbl[-1]


@cached
def count_construct_mem(target_str, str_array):
    """Counts number of ways the target_str can be built using
    words in str_array
    """

    if target_str == "":
        return 1

    tot_count = 0
    for a_str in str_array:
        if target_str.startswith(a_str):
            tot_count += count_construct_mem(
                target_str.split(a_str, 1)[1], str_array
            )

    return tot_count


def count_construct_tabl(target_str, str_array):
    """Tabulation algorithm for count construct"""

    tbl_len = len(target_str) + 1
    tbl = [0] * (tbl_len)
    tbl[0] = 1

    for indx in range(tbl_len):
        if tbl[indx] != 0:
            for a_str in str_array:
                if target_str[indx:].startswith(a_str):
                    tbl[indx + len(a_str)] += tbl[indx]

    return tbl[-1]


@cached
def all_construct_mem(target_str, str_array):
    """returns all possible ways the target_str can be built using
    words in str_array
    returns empty array if none can be constructed
    """

    if target_str == "":
        return [[]]

    tot_ways = []
    for a_str in str_array:
        if target_str.startswith(a_str):
            sub_ways = all_construct_mem(
                target_str.split(a_str, 1)[1], str_array
            )
            if sub_ways:
                for a_way in sub_ways:
                    tot_ways.append([a_str] + a_way)

    return tot_ways


def all_construct_tabl(target_str, str_array):
    """Tabulation algorithm for all construct"""

    tbl_len = len(target_str) + 1
    tbl = [[] for __ in range(tbl_len)]
    tbl[0] = [[]]

    for indx in range(tbl_len):
        if tbl[indx]:
            for a_str in str_array:
                if target_str[indx:].startswith(a_str):
                    for a_combi in tbl[indx]:
                        tbl[indx + len(a_str)].append(a_combi + [a_str])

    return tbl[-1]


def run_algo(algo_tpl, algo_func, msg):  # pragma: no cover
    """Runs a specific algo given inputs"""

    print(msg)

    for algo_input in algo_tpl:
        print(algo_func(algo_input[0], algo_input[1]))

    print("===========")


def main():  # pragma: no cover
    """For manual testing"""

    test_data = (
        ("purple", ("purp", "p", "ur", "le", "purpl")),
        ("abcdef", ("ab", "abc", "cd", "def", "abcd")),
        ("enterapotentpot", ("a", "p", "ent", "enter", "ot", "o", "t")),
        ("skateboard", ("b0", "rd", "ate", "t", "ska", "sk", "boar")),
        (
            "eeeeeeeeeeeeeeeeeeeeef",
            ("e", "ee", "eee", "eeee", "eeeee", "eeeeee"),
        ),
    )

    run_algo(test_data, can_construct_mem, "Memoized can construct")
    run_algo(test_data, can_construct_tabl, "Tabulated can construct")
    run_algo(test_data, count_construct_mem, "Memoized count construct")
    run_algo(test_data, count_construct_tabl, "Tabulated count construct")
    run_algo(test_data, all_construct_mem, "Memoized all construct")
    run_algo(test_data, all_construct_tabl, "Tabulated all construct")


if __name__ == "__main__":
    main()
