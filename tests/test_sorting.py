"""Testing of sorting algorithms"""
import pytest
from hypothesis import given
from hypothesis import strategies as st
from grokking_algo.sorting import selectionsort, quicksort, quicksort_worstcase


@given(st.lists(st.integers()))
@pytest.mark.parametrize("algo", [selectionsort, quicksort])
def test_sorting_algo(algo, array):
    """Sorting algorithms generic test"""
    sorted_array = algo(array)
    assert len(sorted_array) == len(array)
    assert sorted_array == sorted(array)


def test_quicksort_worstcase():
    """Tests the worstcase quicksort algo."""
    array = [100, 5, 20, -1, 75]
    sorted_array = [-1, 5, 20, 75, 100]
    assert sorted_array == quicksort_worstcase(array)
