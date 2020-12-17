"""
Tests for the measure module
"""

import molecool as mol
import numpy as np
import pytest

def test_calculate_distance():

    r1 = np.array([0.0, 0.0, 0.0])
    r2 = np.array([0.0, 1.0, 0.0])

    expect_dist = 1.0
    calculate_dist = mol.calculate_distance(r1, r2)

    assert expect_dist == calculate_dist

def test_angle():
    r1 = np.array([0.0, 0.0, -1.0])
    r2 = np.array([0.0, 0.0, 0.0])
    r3 = np.array([1.0, 0.0, 0.0])

    expect_value = 90.0
    calculate_value = mol.calculate_angle(r1, r2, r3, degrees=True)

    assert pytest.approx(expect_value, abs=1e-2) == calculate_value
