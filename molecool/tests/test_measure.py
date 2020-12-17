"""
Tests for the measure module
"""

import molecool as mol
import numpy as np

def test_calculate_distance():

    r1 = np.array([0.0, 0.0, 0.0])
    r2 = np.array([0.0, 1.0, 0.0])

    expect_dist = 1.0
    calculate_dist = mol.calculate_distance(r1, r2)

    assert expect_dist == calculate_dist
