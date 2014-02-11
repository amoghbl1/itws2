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

class ReverseListIterator(object):
	def __init__(self, dll):
		#where dll is a doubly linked list object
		self.dll = dll
		self.mytail = self.dll.tail
	def __iter__(self):
		return self
	def next(self):
		ret = self.mytail
		if ret != None:
			self.mytail = self.mytail.prev
			return ret.val
		else:
			raise StopIteration

class ExtendedDoublyLinkedList(DoublyLinkedList):
	def getReverseIterator(self):
		return ReverseListIterator(self)