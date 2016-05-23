class Matrix(object):
    def __init__(self, size, snakes, ladders):
        self.size = size
        self.snakes = snakes
        self.ladders = ladders

    @property
    def transitions(self):
        return range(0, self.size + 1)
