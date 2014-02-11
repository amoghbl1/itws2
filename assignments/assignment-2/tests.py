from window import Window
from window import AppWindow
from dialogbox import DialogBox
from button import Button
from point import Point
from answer import *

def testAppWIndow():
    aw = AppWindow("Test Application", Point(10, 10), 200, 100)
    assert(aw.get_title() == "Test Application")
    assert(aw.get_size() == (200, 100))

def testDialog():
    aw = AppWindow("Test Application", Point(10, 10), 200, 100)
    dlg = DialogBox(aw, "Test Dialog", Point(100, 50), 50, 50)
    assert(dlg.get_title() == "Test Dialog")
    assert(dlg.get_size() == (50, 50))
    
def testRadioButtonGroup():
	
testAppWIndow()
testDialog()
testRadioButtonGroup()