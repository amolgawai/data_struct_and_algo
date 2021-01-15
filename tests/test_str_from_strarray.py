"""Tests for alorithms to construct a string fom array of strings """
import pytest
from dynamic_prog.str_from_strarray import (
    can_construct_mem,
    can_construct_tabl,
    count_construct_mem,
    count_construct_tabl,
    all_construct_mem,
    all_construct_tabl,
)


@pytest.fixture
def input_data_true():
    """Inut data for truth values"""

    return (
        ("purple", ("purp", "p", "ur", "le", "purpl"), 2),
        ("abcdef", ("ab", "abc", "cd", "def", "abcd"), 1),
        ("enterapotentpot", ("a", "p", "ent", "enter", "ot", "o", "t"), 4),
    )


@pytest.fixture
def input_data_false():
    """Input data for false values"""

    return (
        ("skateboard", ("bo", "rd", "ate", "t", "ska", "sk", "boar")),
        ("eeeeeeeeeeeeeeeeeeeeef", ("e", "ee", "eee", "eeee", "eeeee", "eeeeee")),
    )


def test_can_construct_true(input_data_true):
    """Tests for truth of can construct algorithms"""

    for a_data in input_data_true:
        assert can_construct_mem(a_data[0], a_data[1]) is True
        assert can_construct_tabl(a_data[0], a_data[1]) is True


def test_can_construct_false(input_data_false):
    """Tests for truth of can construct algorithms"""

    for a_data in input_data_false:
        assert can_construct_mem(a_data[0], a_data[1]) is False
        assert can_construct_tabl(a_data[0], a_data[1]) is False


def test_count_construct_true(input_data_true):
    """Tests for truth of count construct algorithms"""

    for a_data in input_data_true:
        assert count_construct_mem(a_data[0], a_data[1]) == a_data[2]
        assert count_construct_tabl(a_data[0], a_data[1]) == a_data[2]


def test_count_construct_false(input_data_false):
    """Tests for truth of count construct algorithms"""

    for a_data in input_data_false:
        assert count_construct_mem(a_data[0], a_data[1]) == 0
        assert can_construct_tabl(a_data[0], a_data[1]) == 0


def test_all_construct_true(input_data_true):
    """Tests for truth of all construct algorithms"""

    for a_data in input_data_true:
        assert len(all_construct_mem(a_data[0], a_data[1])) == a_data[2]
        assert len(all_construct_tabl(a_data[0], a_data[1])) == a_data[2]


def test_all_construct_false(input_data_false):
    """Tests for truth of count construct algorithms"""

    for a_data in input_data_false:
        assert not all_construct_mem(a_data[0], a_data[1])

    # the tabulation algo has exponential complexity so avoid large test case
    first_data = input_data_false[0]
    assert not all_construct_tabl(first_data[0], first_data[1])
