class Matrix(object):
    def __init__(self, size, snakes, ladders):
        self.size = size
        self.snakes = snakes
        self.ladders = ladders

    @property
    def transitions(self):
        l = [ range(i+1, i+7) for i in range(0, self.size + 1) ]
        return l
