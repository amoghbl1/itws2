from window import *

class ChildWindowIterator(object):
	def __init__(self, container):
		self.children = container.children
	def __iter__(self):
		return iter(self.children)

class RadioButtonGroup(Container):
	class RadioButton(object):
		def __init__(self, value):
			self.chosen = False
			self.value = value
		def click(self):
			self.chosen = True

	# radioButtons is a list or tupple of the radio buttons that the radio button group must hold and the first one is selected to be true.
	def __init__(self, parent, title, top_left, w, h, radioButtons):
		assert(parent is not None)
		assert(isinstance(parent, (AppWindow)))
		assert(isinstance(top_left, Point))
		assert(radioButtons.__len__()>=1)
		Container.__init__(self, parent, title, top_left, w, h)
		self.RadioButtons = []
		for i in radioButtons:
			self.RadioButtons.append(self.RadioButton(i))
		self.RadioButtons[0].click()

def CheckCycle(obj):
	visited = []
	try:
		parent = obj.parent
	except AttributeError:
		parent = None
	while parent != None:
		if parent in visited:
			return False
		visited.append(parent)
		try:
			parent = parent.parent
		except AttributeError:
			parent = None
	return True #means that there is no cycle

def CheckParent(obj, par):
	try:
		parent = obj.parent
	except AttributeError:
		parent = None
	while parent != None:
		if parent == par:
			return True
		try:
			parent = parent.parent
		except AttributeError:
			parent = None
	return False