"""Tests for various implementations of fibonacci"""
import re
from dynamic_prog.fibonacci import fib_rec_brut_force, fib_rec_memoize, fib_tab


def get_num_fib_pairs(input_fl_name):
    """Gets the test pair of fibonacci
    Keyword Arguments:
    input_fl_name -- file containing data
    """

    with open(input_fl_name) as input_f:
        fibs = list()
        for line in input_f.readlines():
            num, fib = re.findall(r"\d+", line)
            fibs.append((int(num), int(fib)))

    return fibs


def test_fib_brut_force(get_test_data_path):
    """Tests brut force fibonacci"""
    num_fib_pairs = get_num_fib_pairs(get_test_data_path("fibonacci.txt"))
    for num_fib in filter(lambda x: x[0] <= 8, num_fib_pairs):
        assert num_fib[1] == fib_rec_brut_force(num_fib[0])


def test_fib_rec_memoize(get_test_data_path):
    """Tests the recursive memoized fibonacci function"""
    num_fib_pairs = get_num_fib_pairs(get_test_data_path("fibonacci.txt"))
    for num_fib in num_fib_pairs:
        assert num_fib[1] == fib_rec_memoize(num_fib[0])


def test_fib_tab(get_test_data_path):
    """Tests the recursive memoized fibonacci function"""
    num_fib_pairs = get_num_fib_pairs(get_test_data_path("fibonacci.txt"))
    for num_fib in num_fib_pairs:
        assert num_fib[1] == fib_tab(num_fib[0])
