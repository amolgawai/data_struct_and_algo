"""Helper functions for testing"""
import os
import pytest


FIXTURE_DIR = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    "test_data",
)


@pytest.fixture()
def get_test_data_path():
    """Gets the path of test data file
    Keyword Arguments:
    file_name -- test data file name
    """

    def test_d_path(file_name):
        return os.path.join(FIXTURE_DIR, file_name)

    return test_d_path
