
__all__ = ["length","normalize","dot_product","cross_product"]

#all the functions have been written assuming that the vector is given by point2 - point1
#this is the length vector which tells us the length of the given vector!
def length(vector):
	distance = (vector[0][0] - vector[1][0])**2 + (vector[0][1] - vector[1][1])**2 + (vector[0][2] - vector[1][2])**2
	distance = distance**0.5
	return distance

def normalize(vector):
	length_of_vector = length(vector)
	x = vector[1][0] - vector[0][0]
	y = vector[1][1] - vector[1][0]
	z = vector[1][2] - vector[0][2]
	"""
	if x < 0:
		x = x*-1
	if y < 0:
		y = y*-1
	"""
	if length_of_vector != 0:
		return (x/length_of_vector, y/length_of_vector, z/length_of_vector)
	else:
		return (0,0)

def dot_product(vector1, vector2):
	x1 = vector1[1][0] - vector1[0][0]
	x2 = vector2[1][0] - vector2[0][0]
	y1 = vector1[1][1] - vector1[1][0]
	y2 = vector2[1][1] - vector2[1][0]
	z1 = vector1[1][2] - vector2[2][2]
	z2 = vector2[2][2] - vector2[1][2]
	return x1*x2 + y1*y2 + z1*z2

def cross_product(vector):
	x1 = vector1[1][0] - vector1[0][0]
	x2 = vector2[1][0] - vector2[0][0]
	y1 = vector1[1][1] - vector1[1][0]
	y2 = vector2[1][1] - vector2[1][0]
	z1 = vector1[1][2] - vector2[2][2]
	z2 = vector2[2][2] - vector2[1][2]
	return ((y1*z2 - z1*y2), (x1*z2 - z1*x2), (x1*y2 - y1*x2))
