class Window(object):
    STATE_NORMAL    = 0x1
    STATE_MINIMIZED = 0x2
    STATE_MAXIMIZED = 0x4

    FOCUS_FOREGROUND = 0x1
    FOCUS_BACKGROUND = 0x2

    def __init__(self, parent, title, top_left, h, w):
    	self.parent = parent
        self.title = tirtle
        self.top_left = top_left
        self.height = h
        self.width = w
        self.state = STATE_NORMAL

    def get_title(self):
        return self.title
    
    def resize(self, w, h):
        self.width = w
        self.height = h

    def get_size(self):
        return (self.width, self.height)

    def get_state(self):
    	return self.state

    def ser_state(self, state):
    	if state != STATE_NORMAL or state != STATE_MINIMIZED or \
    	                                   state != STATE_MAXIMIZED:
            state = STATE_NORMAL
        
        self.state = state


