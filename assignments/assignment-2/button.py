from window import ChildWindow
from window import AppWindow
from point import Point
from window import BadArgumentError
from dialogbox import *

# Button class is also given an extra parameter value while it's implementation.
# Where the value can be CANCEL or ACCEPT
# don't know why the asserts were commented out, they are necessair
class Button(ChildWindow):
    def __init__(self, parent, title, top_left, w, h, value):
        assert(parent is not None)
        assert(isinstance(parent, (DialogBox)))
        assert(isinstance(top_left, Point))
        if parent is None or not isinstance(parent, Container):
        	raise BadArgumentError("Expecting a valid parent window")

        if (value != "CANCEL") and (value != "ACCEPT"):
        	raise BadArgumentError("Expecting a valid button value")
        self.value = value
        Window.__init__(self, parent, title, top_left, w, h)

# Assuming that the parent of this button is going to be a dialogbox object.
    def click(self):
    	if self.value == "ACCEPT":
    		self.parent.accept()
    	elif self.value == "CANCEL":
    		self.parent.cancel()