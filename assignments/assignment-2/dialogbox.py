from window import Window, Container, AppWindow, ChildWindow
from point import Point
from window import BadArgumentError

class DialogBox(Container, ChildWindow):
    def __init__(self, parent, title, top_left, w, h):
    	assert(parent is not None)
    	assert(isinstance(parent, (AppWindow)))
        assert(isinstance(top_left, Point))
        self.buttonState = None
        Container.__init__(self, parent, title, top_left, w, h)

    def accept(self):
    	self.buttonState = "ACCEPT"

    def cancel(self):
    	self.buttonState = "CANCEL"
