from window import ChildWindow, Container, Window
from window import AppWindow
from point import Point
from window import BadArgumentError

""" Unicode enabled text widget,"""
class TextBox(ChildWindow):
    def __init__(self, parent, title, top_left, w, h):
        assert(parent is not None)
        assert(isinstance(parent, (AppWindow)))
        assert(isinstance(top_left, Point))
        if parent is None or not isinstance(parent, Container):
        	raise BadArgumentError("Expecting a valid parent window")
        
        Window.__init__(self, parent, title, top_left, w, h)

    def setText(self, text):
    	self.text = text

    def getText(self):
    	return self.text

    def validate(self, validator):
    	#assuming that validator is a string of the type int, float, string
        return isinstance(self.text, validator)


def isaNumber(text):
	return isinstance(text, int)

def isaFloat(text):
	return isinstance(text, float)

def isaURL(text):
    flag = False
    if "http" in text or "https" in text:
        flag = True
    else:
        flag = False
    if ".com" in text or ".in" in text or ".org" in text or ".net" in text:
        flag = True
    else:
        flag = False
    return flag