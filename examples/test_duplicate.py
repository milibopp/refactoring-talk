from duplicate import *

def test_orthogonal():
    assert abs(theta([0, 1], [1, 0]) - 90) < 0.01

def test_45deg():
    assert abs(theta([1, 1], [1, 0]) - 45) < 0.01

def test_3d_vector():
    assert abs(theta([0, 0, 1], [0, 1, 0]) - 90) < 0.01
