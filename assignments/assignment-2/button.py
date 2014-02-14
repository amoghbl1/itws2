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
            clicker = OK()
            clicker.click(self.parent)
        elif self.value == "CANCEL":
            clicker = Cancel()
            clicker.click(self.parent)

class OK(object):
    def __init__(self):
        pass
    def click(self, par):
        par.accept()

class Cancel(object):
    def __init__(self):
        pass
    def click(self, par):
        par.cancel()


class RadioButtonGroup(Container):

    def __init__(self, parent, title, top_left, w, h):
        assert(isinstance(top_left, (Point)))
        Container.__init__(self, parent, title, top_left, w, h)
        self.RadioButtons = []

    def addButton(self, button):
        self.RadioButtons.append(button)
        self.unClickAll()
        self.RadioButtons[0].click()

    def unClickAll(self):
        for i in self.RadioButtons:
            i.unClick()

class RadioButton(Container):
    RADIO_ACTIVE = 0x1
    RADIO_INACTIVE = 0x0
    
    def __init__(self, parent, title, top_left, w, h):
        self.parent=parent
        self.state = self.RADIO_INACTIVE
        Container.__init__(self, parent, title, top_left, w, h)
        self.parent.addButton(self)
    
    def click(self):
        self.parent.unClickAll()
        self.state = self.RADIO_ACTIVE
    
    def unClick(self):
        self.state = self.RADIO_INACTIVE

    def getState(self):
        return self.state