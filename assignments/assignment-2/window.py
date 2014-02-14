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
        if self.focus == False:
            self.focus = True
            return True
        return False

    def removeFocus(self):
        if self.focus == True:
            self.focus = False
            return True
        return False
    
    def hasFocus(self):
        return self.focus
    
    def minimize(self):
        if self.state != Window.STATE_MINIMIZED:
            self.state = Window.STATE_MINIMIZED
            return True
        return False

    def maximize(self):
        if self.state != Window.STATE_MAXIMIZED:
            self.state = Window.STATE_MAXIMIZED
            return True
        return False


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

    def childIterator(self):
        newIter = ChildWindowIterator(self)
        return newIter.__iter__()

    def CheckCycle(self):
        visited = []
        try:
            parent = self.parent
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

    def CheckParent(self, par):
        try:
            parent = self.parent
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

class ChildWindowIterator(object):
    def __init__(self, container):
        self.children = container.children
    def __iter__(self):
        return iter(self.children)

class ChildWindow(Window):
    def __init__(self, parent, title, top_left, w, h):
        if parent is None or not isinstance(parent, Container):
            raise BadArgumentError("Expecting a valid parent window instance")
        Window.__init__(self, parent, title, top_left, w, h)



class AppWindow(Container):
    def __init__(self, title, top_left = Point(0, 0), w=40, h=40):
        Container.__init__(self, None, title, top_left, w, h)