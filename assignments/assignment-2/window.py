from point import Point


class BadArgumentError(Exception):
    def __init__(self, cause):
        Exception.__init__(self, cause)


class Window(object):
    STATE_NORMAL    = 0x1
    STATE_MINIMIZED = 0x2
    STATE_MAXIMIZED = 0x4

    FOCUS_FOREGROUND = 0x1
    FOCUS_BACKGROUND = 0x2

    def __init__(self, parent, title, top_left, w, h):
    	self.parent = parent
        self.title = title
        self.top_left = top_left
        self.height = h
        self.width = w
        self.state = Window.STATE_NORMAL
        self.focus = True # as the window state is normal, I assume that the normal state for it means that it has focus!

    def get_title(self):
        return self.title
    
    def resize(self, w, h):
        self.width = w
        self.height = h

    def get_size(self):
        return (self.width, self.height)

    def get_state(self):
    	return self.state

    # def set_state(self, state):
    # 	if state != Window.STATE_NORMAL or state != Window.STATE_MINIMIZED or \
    # 	                                   state != Window.STATE_MAXIMIZED:
    #         state = Window.STATE_NORMAL
        
    #     self.state = state

    def __str__(self):
    	return "(Window: (%s), (width: %d, height: %d)" % (self.title, self.width, self.height)

    #this window has no knowledge of other windows and we assume that during it's use, the designer ensures that there is no focus on other window,
    #hence the removeFocus function has been implemented in order to help achieve this
    def setFocus(self):
        self.focus = True

    def removeFocus(self):
        self.focus = False
    
    def hasFocus():
        return self.focus
    
    def minimize():
        self.state = Window.STATE_MINIMIZED

    def maximize():
        self.state = Window.STATE_MAXIMIZED


class Container(Window):
    def __init__(self, parent, title, top_left, w, h):
        Window.__init__(self, parent, title, top_left, w, h)
        self.children = []

    def addChildWindow(self, childWindow):
        if self.checkParent(childWindow):
            if (isinstance(childWindow, ChildWindow)):
                self.children.append(childWindow)
                return True
            raise BadArgumentError("Expecting a valid child window instance")
        else:
            raise BadArgumentError("The ChildWindow already has a parent")
            


    def checkParent(self, childWindow):
        if childWindow.parent != self:
            return False
        return True

class ChildWindow(Window):
    def __init__(self, parent, title, top_left, w, h):
        if parent is None or not isinstance(parent, Container):
            raise BadArgumentError("Expecting a valid parent window instance")

        Window.__init__(self, parent, title, top_left, w, h)



class AppWindow(Container):
    def __init__(self, title, top_left = Point(0, 0), w=40, h=40):
        Container.__init__(self, None, title, top_left, w, h)
