""" tests for the sum_in_array.py functions"""
import pytest
from dynamic_prog.sum_in_array import (
    can_sum_mem,
    can_sum_tabl,
    how_sum_mem,
    how_sum_tabl,
    best_sum_mem,
    best_sum_tabl,
)


@pytest.fixture
def sum_input_true():
    """Reurns the input for positive case of sum function tests"""

    return ((0, 7, 10, 300), (5, 4, 3, 7))


@pytest.fixture
def sum_input_false():
    """Reurns the input for positive case of sum function tests"""

    return ((2, 5, 50, 300), (7, 14))


def test_can_sum_true(sum_input_true):
    """ Tests the memoized can sum function"""
    target_sums, array = sum_input_true

    for target_sum in target_sums:
        assert can_sum_mem(target_sum, array) is True
        assert can_sum_tabl(target_sum, array) is True


def test_can_sum_false(sum_input_false):
    """ Tests the memoized can sum function"""
    target_sums, array = sum_input_false

    for target_sum in target_sums:
        assert can_sum_mem(target_sum, array) is False
        assert can_sum_tabl(target_sum, array) is False


def test_how_sum_true(sum_input_true):
    """Tests positive case of how sum function"""
    target_sums, array = sum_input_true

    for target_sum in target_sums:
        res_mem = how_sum_mem(target_sum, array)
        assert sum(res_mem) == target_sum
        res_tabl = how_sum_tabl(target_sum, array)
        assert sum(res_tabl) == target_sum


def test_how_sum_false(sum_input_false):
    """Tests negative case of how sum function"""
    target_sums, array = sum_input_false

    for target_sum in target_sums:
        assert how_sum_mem(target_sum, array) is None
        assert how_sum_tabl(target_sum, array) is None


def test_best_sum_true(sum_input_true):
    """Tests positive case of how sum function"""
    target_sums, array = sum_input_true

    for target_sum in target_sums:
        res_mem = best_sum_mem(target_sum, array)
        assert sum(res_mem) == target_sum
        res_tabl = best_sum_tabl(target_sum, array)
        assert sum(res_tabl) == target_sum
        if target_sum == 7:
            assert len(res_mem) == 1
            assert len(res_tabl) == 1
        if target_sum == 10:
            assert len(res_mem) == 2
            assert len(res_tabl) == 2


def test_best_sum_false(sum_input_false):
    """Tests negative case of how sum function"""
    target_sums, array = sum_input_false

    for target_sum in target_sums:
        assert best_sum_mem(target_sum, array) is None
        assert best_sum_tabl(target_sum, array) is None
