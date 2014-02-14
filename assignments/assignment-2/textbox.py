from window import ChildWindow, Container, Window
from window import AppWindow
from point import Point
from window import BadArgumentError

""" Unicode enabled text widget,"""
class TextBox(ChildWindow):
    def __init__(self, parent, title, top_left, w, h):
        assert(parent is not None)
        """
        try:
            assert(isinstance(parent, (AppWindow)))
        except AssertionError:
            raise BadArgumentError("Expecting an AppWindow as parent")
        """
        assert(isinstance(top_left, Point))
        if parent is None or not isinstance(parent, Container):
        	raise BadArgumentError("Expecting a valid parent window")
        self.text=""
        Window.__init__(self, parent, title, top_left, w, h)

    def setText(self, text):
    	self.text = str(text)

    def getText(self):
    	return str(self.text)

    def validate(self, validator):
    	#assuming that validator is a string of the type int, float, string
        return validator(self.text)


def isaNumber(text):
    if isinstance(text, int):
        return True
    try:
        text = int(text)
    except ValueError:
        return False
    return True

def isaFloat(text):
    if isinstance(text, float):
        return True
    text = str(text)
    if "." not in text:
        return False
    try:
        text = float(text)
    except ValueError:
        return False
    return True

def isaURL(text):
    if (text.startswith("http://") or text.startswith("https://")) and "." in text:
        return True
    return False