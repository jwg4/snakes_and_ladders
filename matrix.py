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
        return l
