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

        
class TestMatrixWithOneSnake(unittest.TestCase):
    def setUp(self):
        self.size = 6
        self.snakes = [(5, 2)]
        matrix = Matrix(self.size, self.snakes, [])
        self.transitions = matrix.transitions

    def test_that_nothing_transitions_to_the_head_of_the_snake(self):
        for t in self.transitions:
            self.assertNotIn(5, t)

class TestMatrixWithOneLadder(unittest.TestCase):
    def setUp(self):
        self.size = 6
        self.ladders = [(2, 5)]
        matrix = Matrix(self.size, self.ladders, [])
        self.transitions = matrix.transitions

    def test_that_nothing_transitions_to_the_foot_of_the_ladder(self):
        for t in self.transitions:
            self.assertNotIn(2, t)
