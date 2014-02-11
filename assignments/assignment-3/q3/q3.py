class Rectangle(object):
	def __init__(self, lbp, width, height):
		self.left_bottom_point = lbp
		self.width = width
		self.height = height
	def intersect(self, rectangle_object):
		if self.left_bottom_point[0] > rectangle_object.left_bottom_point[0]:
			if rectangle_object.left_bottom_point[0] + rectangle_object.width > self.left_bottom_point[0]:
				return True
		elif rectangle_object.left_bottom_point[0] > self.left_bottom_point[0]:
			if self.left_bottom_point[0] + self.width > rectangle_object.left_bottom_point[0]:
				return True
		elif self.left_bottom_point[1] > rectangle_object.left_bottom_point[1]:
			if rectangle_object.left_bottom_point[1] + rectangle_object.height > self.left_bottom_point[1]:
				return True
		elif rectangle_object.left_bottom_point[1] > self.left_bottom_point[1]:
			if self.left_bottom_point[1] + self.height > rectangle_object.left_bottom_point[1]:
				return True
		return False

class WordIterator(object):
	def __init__(self,string):
		self.words = string.split()
		pass
	def __iter__(self):
		return self
	def next(self):
		try:
			return self.words.pop(0)
			pass
		except Exception, e:
			raise StopIteration

class PointIterator(object):
	"My linear interpolation is supposed to give 10 points."
	def __init__(self, p1, p2):
		self.p1 = p1
		self.p2 = p2
		self.movx = (p2[0]-p1[0])/10
		self.movy = (p2[1]-p1[1])/10
		pass
	def __iter__(self):
		return self
	def next(self):
		if self.p1[0] != self.p2[0]:
			self.p1 = (self.p1[0]+self.movx, self.p1[1]+self.movy)
			return (self.p1[0], self.p1[1])
		else:
			raise StopIteration