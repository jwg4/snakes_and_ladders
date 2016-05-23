import unittest

from matrix import Matrix


class TestMatrix(unittest.TestCase):
    def test_ctor(self):
        size = 6
        matrix = Matrix(size, [], [])
        transitions = matrix.transitions
