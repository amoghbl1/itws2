class InfiniteEven(object):
  def __init__(self): self.n = 0
  def __iter__(self): return self
  def next(self):
    n = self.n 
    self.n += 2
    return n
