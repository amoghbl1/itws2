from q3 import *
a = Rectangle((0,0), 2, 2)
b = Rectangle((1,1), 1, 1)
c = Rectangle((5,6), 1, 1)
assert(a.intersect(b))
if a.intersect(c) == False:
	assert(1)
else:
	assert(0)
w = WordIterator("This is the example for word iterator")
for i in w:
	if i == None:
		assert(0)
	assert(1)
pi = PointIterator((0.00, 0.00), (10.00, 10.00))
for i in pi:
	if i == None:
		assert(0)
	assert(1)
pi = PointIterator((0.00, 0.00), (5.00, 25.00))
for i in pi:
	if i == None:
		assert(0)
	assert(1)
pi = PointIterator((5.00, 25.00), (0.00, 0.00))
for i in pi:
	if i == None: 
		assert(0)
	assert(1)
