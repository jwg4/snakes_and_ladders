import numpy as np


class Matrix(object):
    def __init__(self, size, snakes, ladders):
        self.size = size
        self.snakes = snakes
        self.ladders = ladders

    @property
    def transitions(self):
        l = [ range(i+1, i+7) for i in range(0, self.size + 1) ]
        for i in range(0, self.size + 1):
            s = l[i]
            for j in range(len(s)):
                if s[j] > self.size:
                    s[j] = i
            s.sort()
        for head, tail in self.snakes:
            for t in l:
                for j in range(len(t)):
                    if t[j] == head:
                        t[j] = tail
                t.sort()
        return l

    def _transition_matrix_rows(self):
        for i in self.transitions:
            l = [ 0 for x in range(self.size + 1) ]
            for j in i:
                l[j] = 1/6
            yield l

    @property
    def transition_matrix(self):
        return np.matrix(list(self._transition_matrix_rows()))
