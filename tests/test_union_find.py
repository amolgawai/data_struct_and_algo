"""Tests for Union Find"""
from coursera_algo1.union_find import QuickFindUF, QuickUnionUF


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


def test_quickfind_qf(get_test_data_path):
    input_fl_name = get_test_data_path("tinyUF.txt")
    test_sz, test_unions = get_test_input(input_fl_name)
    qf_uf = QuickFindUF(test_sz)

    for xy_tpl in test_unions:
        qf_uf.union(xy_tpl[0], xy_tpl[1])

    for test_tpl in test_unions:
        assert qf_uf.are_connected(test_tpl[0], test_tpl[1])


def test_quickunion_qf(get_test_data_path):
    input_f_name = get_test_data_path("mediumUF.txt")
    test_sz, test_unions = get_test_input(input_f_name)
    test_uf = QuickUnionUF(test_sz)

    for xy_tpl in test_unions:
        test_uf.union(xy_tpl[0], xy_tpl[1])

    for test_tpl in test_unions:
        assert test_uf.are_connected(test_tpl[0], test_tpl[1])
