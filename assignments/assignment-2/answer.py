from window import *

class ChildWindowIterator(object):
	def __init__(self, container):
		self.children = container.children
	def __iter__(self):
		return iter(self.children)

class RadioButtonGroup(Container, ChildWindow):
	class RadioButton()