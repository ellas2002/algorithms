import pytest
from math import pi
from quickhull import *
import random


def test_finds_determinant():
    assert determinant((1, 2), (3, 1), (2, 3)) == 3


def test_finds_angle():
    assert angle((1, 1), (0, 0), (1, 0)) == pytest.approx(pi / 4)


def test_finds_points_to_left():
    a = (0, 2)
    b = (4, 3)
    points = [(1, 3), (2, 2.5), (2, 1), (3, 4)]
    # Set is used below so that the order in which the points are returned doesn't matter
    assert set(points_to_left(a, b, points)) == {(1, 3), (3, 4)}
    assert set(points_to_left(b, a, points)) == {(2, 1)}


def test_finds_hull():
    points = [(0, 2), (1, 3), (2, 2.5), (4, 3), (2, 1), (3, 4)]
    assert quickhull(points) == [(0, 2), (1, 3), (3, 4), (4, 3), (2, 1)]


def test_finds_complicated_hull():
    random.seed(0)
    points = [(random.randint(0, 99), random.randint(0, 99)) for _ in range(50)]
    assert quickhull(points) == [(0, 78), (11, 92), (12, 93), (17, 96), (49, 97), (85, 80), (90, 77), (81, 26), (70, 1), (11, 10), (8, 24)]
