
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move_by(self, dx, dy):
        self.x += dx
        self.y += dy

    def __str__(self):
        return "{x:%d, y:%d}" % (self.x, self.y)

    def __eq__(self, that):
    	print "eq called!"
    	
    	return self.x == that.x and self.y == that.y

    def __lt__(self, that):
    	print "lt called!"
    	return self.x < that.x and self.y <that.y

    def __gt__(self, that):
    	print "gt called!"
    	return self.x > that.x and self.y > that.y
