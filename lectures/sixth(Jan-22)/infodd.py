class InfiniteOdd(object):
    def __init__(self):
        pass
    def __iter__(self):
        class OddIterator(object):
            def __init__(self):
                self.n = 1
            def next(self):
                r = self.n
                self.n += 2
                return r
            def __iter__(self):
                return self

        return OddIterator()
    
