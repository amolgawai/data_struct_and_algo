"""Tests for grid traveler algorithms"""
import pytest
from dynamic_prog.grid_traveler import (
    grid_travel_rec_brt_frc,
    grid_travel_rec_memzd,
    grid_travel_tab,
)


@pytest.fixture
def grid_paths():
    return [
        ((0, 1), 0),
        ((1, 1), 1),
        ((2, 3), 3),
        ((5, 5), 70),
        ((10, 10), 48620),
        ((18, 18), 2333606220),
        ((50, 100), 4503056131931081050165600532646379362000),
    ]


def test_grid_travel_rec_brt_frc(grid_paths):
    """Tests the brute force algorithm"""

    for grd_path in filter(lambda tpl: tpl[0][0] <= 8 and tpl[0][1] <= 8, grid_paths):
        assert grid_travel_rec_brt_frc(grd_path[0][0], grd_path[0][1]) == grd_path[1]


def test_grid_travel_rec_memzd(grid_paths):
    """Tests the memoized grid traveler algorithm"""

    for grd_path in grid_paths:
        assert grid_travel_rec_memzd(grd_path[0][0], grd_path[0][1]) == grd_path[1]


def test_grid_travel_tab(grid_paths):
    """Tests the tabulation grid traveler algorithm"""

    for grd_path in grid_paths:
        assert grid_travel_tab(grd_path[0][0], grd_path[0][1]) == grd_path[1]
