""" Permutation and Combinations tests"""
from coderbyte_algo.permut_combin import permutations, combinations


def test_combination():
    """Simple test for combinations """

    test_array = ["a", "b", "c"]

    result = combinations(test_array)
    combi_empty_single = [lst for lst in result if len(lst) < 2]
    combi_two = [lst for lst in result if len(lst) == 2]
    combi_three = [lst for lst in result if len(lst) == 3]

    assert len(result) == 8
    assert len(combi_empty_single) == 4
    assert len(combi_two) == 3
    assert len(combi_three) == 1


def test_permutations():
    """ Simple tst for permutations"""
    test_array = ["a", "b", "c"]
    expected = [
        ["a", "b", "c"],
        ["b", "a", "c"],
        ["b", "c", "a"],
        ["a", "c", "b"],
        ["c", "a", "b"],
        ["c", "b", "a"],
    ]

    result = permutations(test_array)

    assert len(result) == 6
    for a_permut in expected:
        assert a_permut in result
