import unittest

from matrix import Matrix


class TestSimpleMatrix(unittest.TestCase):
    def setUp(self):
        self.size = 6
        matrix = Matrix(self.size, [], [])
        self.transitions = matrix.transitions

    def test_ctor_and_basic_transitions(self):
        self.assertEqual(len(self.transitions), self.size+1)
        self.assertEqual(self.transitions[0], [1,2,3,4,5,6])

    def test_transitions_near_the_finish(self):
        self.assertEqual(self.transitions[1], [1,2,3,4,5,6])

    def test_transitions_even_nearer_the_finish(self):
        self.assertEqual(self.transitions[4], [4,4,4,4,5,6])
