"""
An example to show how objects can implement protocols that 
enable them to be used in comparison and equality tests, and also
make them printable.
"""

"Implementing __str__ enable Point instances to be meaningfully used with"
"print statement and str() functions."
"Implementing __eq__(), __lt__(), and __gt__() enables them to be compared."

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move_by(self, dx, dy):
        self.x += dx
        self.y += dy

    def __str__(self):
        return "(x: %d, y: %d)" % (self.x, self.y)

    def __eq__(self, that):
        return self.x == that.x and self.y == that.y

    def __lt__(self, that):
        return self.x < that.x and self.y <that.y

    def __gt__(self, that):
        return self.x > that.x and self.y > that.y


"Test cases"
if __name__ == '__main__':
    p1 = Point(10, 20)
    p2 = Point(10, 20)
    q = Point(100, 200)

    assert(p1 == p2)
    assert(p1 <= p2)
    assert(p2 >= p1)
    assert(p1 != q)
    assert(p1 < q)
    assert(p1 <= q)
    assert(q >= p2)

    assert(str(p1) == '(x: 10, y: 20)') 
    assert(str(p1) == str(p2))
    assert(repr(q) == repr(q))

