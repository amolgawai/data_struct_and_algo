"""Tests for Union Find"""
import os
from coursera_algo1.union_find import QuickFindUF, QuickUnionUF


FIXTURE_DIR = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    "test_data",
)


def get_test_input(input_f_name):
    """Gets test inpt from file
    Keyword Arguments:
    input_f_name -- filename containing data
    """

    with open(input_f_name) as input_f:
        uf_data = input_f.readlines()

    uf_size = int(uf_data[0])
    uf_unions = list()
    for x_y in uf_data[1:]:
        x, y = x_y.split()
        uf_unions.append((int(x), int(y)))

    return (uf_size, uf_unions)


def test_quickfind_qf():
    input_fl_name = os.path.join(FIXTURE_DIR, "tinyUF.txt")
    test_sz, test_unions = get_test_input(input_fl_name)
    qf_uf = QuickFindUF(test_sz)

    for xy_tpl in test_unions:
        qf_uf.union(xy_tpl[0], xy_tpl[1])

    for test_tpl in test_unions:
        assert qf_uf.are_connected(test_tpl[0], test_tpl[1])


def test_quickunion_qf():
    input_f_name = os.path.join(FIXTURE_DIR, "mediumUF.txt")
    test_sz, test_unions = get_test_input(input_f_name)
    test_uf = QuickUnionUF(test_sz)

    for xy_tpl in test_unions:
        test_uf.union(xy_tpl[0], xy_tpl[1])

    for test_tpl in test_unions:
        assert test_uf.are_connected(test_tpl[0], test_tpl[1])
