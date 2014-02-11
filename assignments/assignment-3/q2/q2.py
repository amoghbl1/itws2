from q1 import *

class ForwardListIterator(object):
	def __init__(self, dll):
		#where dll is a doubly linked list object
		self.dll = dll
		self.myhead = self.dll.head
	def __iter__(self):
		return self
	def next(self):
		ret = self.myhead
		if ret != None:
			self.myhead = self.myhead.next
			return ret.val
		else:
			raise StopIteration