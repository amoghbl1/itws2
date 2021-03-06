from window import Window, BadArgumentError
from window import AppWindow
from dialogbox import DialogBox
from button import *
from point import Point
from textbox import *

def testAppWIndow():
    aw = AppWindow("Test Application", Point(10, 10), 200, 100)
    assert(aw.get_title() == "Test Application")
    assert(aw.get_size() == (200, 100))
    assert(Container.CheckCycle(aw)) #Checks if there is a cycle in the window hierarchy, this can be used 

def testDialog():
    aw = AppWindow("Test Application", Point(10, 10), 200, 100)
    dlg = DialogBox(aw, "Test Dialog", Point(100, 50), 50, 50)
    but1 = Button(dlg, "Accept", Point(100, 50), 50, 50, "ACCEPT")
    but2 = Button(dlg, "Cancel", Point(100, 50), 50, 50, "CANCEL")
    assert(dlg.buttonState==None)
    but1.click()
    assert(dlg.getState()==DialogBox.STATE_ACCEPT)
    but2.click()
    assert(dlg.getState()==DialogBox.STATE_CANCEL)
    assert(dlg.get_title() == "Test Dialog")
    assert(dlg.get_size() == (50, 50))
    # The button clicked state is initially None and depending on which button is clicked (onClick()), the value of buttonState is changed.
    assert(aw.CheckCycle()) # use this function to check if there exists a cycle in the current hierarchy
    
def testRadioButtonGroup():
	aw = AppWindow("Test Application", Point(10, 10), 200, 100)
	aw1 = AppWindow("Test Application1", Point(11, 11), 201, 101)
	rbg = RadioButtonGroup(aw, "Test Dialog", Point(100, 50), 50, 50)
	rbg1 = RadioButtonGroup(aw1, "Test Dialog1", Point(100, 50), 50, 50)
	rb1 = RadioButton(rbg1, "one", Point(100, 50), 50, 50)
	rb2 = RadioButton(rbg1, "two", Point(100, 50), 50, 50)
	rb3 = RadioButton(rbg1, "three", Point(100, 50), 50, 50)
	assert(rb1.getState()==RadioButton.RADIO_ACTIVE)
	assert(rb2.getState()==RadioButton.RADIO_INACTIVE)
	assert(rb3.getState()==RadioButton.RADIO_INACTIVE)
	assert(aw.CheckCycle)
	assert(rbg.CheckParent(aw)) # use this function before adding something as a child in order to enforce the invariant that there are no cycles in the 
	assert(rbg.CheckParent(aw1)==False) # Window hierarchy
	assert(rbg1.CheckParent(aw1))
	assert(rbg1.CheckParent(aw)==False)

def testTextBox():
	aw = AppWindow("Test Application", Point(10, 10), 200, 100)
	tb = TextBox(aw, "Test Dialog", Point(100, 50), 50, 50)
	tb.setText("Test Text Box")
	assert(tb.getText() == "Test Text Box")
	assert(tb.validate(isaNumber) == False)
	assert(tb.validate(isaFloat) == False)
	assert(tb.validate(isaFloat) == False)
	assert(isaNumber(1))
	assert(isaNumber("a")==False)
	assert(isaFloat("a")==False)
	assert(isaFloat(1)==False)
	assert(isaFloat(1.0))
	assert(isaURL("http://www.google.com"))
	assert(isaURL("testURL") == False)

def testChildWindow():
	aw = AppWindow("AppWindow", Point(10, 10), 200, 100)
	cont = Container(aw, "Container", Point(10, 10), 200, 100)
	cw1 = ChildWindow(cont, "ChildWindow1", Point(10, 10), 200, 100)
	cw2 = ChildWindow(aw, "ChildWindow2", Point(10, 10), 200, 100)
	assert(cont.addChildWindow(cw1)) # this asserts that a child window is only part of one parent window, by throwing an error if the child window has a different 
									 # parent than the one that it is trying to be added to
	try:
		assert(cont.addChildWindow(cw2))
	except BadArgumentError, e:
		if str(e) == "The ChildWindow already has a parent":
			assert(1)
		else:
			assert(0)

testAppWIndow()
testDialog()
testRadioButtonGroup()
testTextBox()
testChildWindow()
# The DialogBox class also needs to be initiated via Container and therefore by validating the parent child relationship before adding children to a Container,
# we have made sure that a child can be part of only one parent and therefore resolved any issue that may have arised due to multiple windows having the same child.