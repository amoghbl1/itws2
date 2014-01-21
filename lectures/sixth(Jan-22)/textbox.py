from window import ChildWindow
from window import AppWindow
from point import Point
from window import BadArgumentError

""" Unicode enabled text widget,"""
class TextBox(ChildWindow):
    def __init__(self, parent, title, top_left, w, h):
        #assert(parent is not None)
        #assert(isinstance(parent, (AppWindow)))
        #assert(isinstance(top_left, Point))
        if parent is None or not isinstance(parent, Container):
        	raise BadArgumentError("Expecting a valid parent window")
        
        Window.__init__(self, parent, title, top_left, w, h)

    def setText(self, text):
    	raise NotImplementedError()

    def getText(self):
    	raise NotImplementedError()

    def validate(self, validator):
    	raise NotImplementedError()


def isaNumber(text):
	raise NotImplementedError()

def isaFloat(text):
	raise NotImplementedError()

def isaURL(text):
	raise NotImplementedError()

