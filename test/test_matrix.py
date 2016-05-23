import unittest

from matrix import Matrix


class TestMatrix(unittest.TestCase):
    def test_ctor(self):
        size = 6
        matrix = Matrix(size, [], [])
        transitions = matrix.transitions
        self.assertEqual(len(transitions), size+1)
        self.assertEqual(transitions[0], [1,2,3,4,5,6])
