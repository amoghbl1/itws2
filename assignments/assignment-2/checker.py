from window import Window, Container, AppWindow, ChildWindow
from point import Point
from dialogbox import DialogBox
from textbox import TextBox, isaNumber, isaFloat, isaURL
from button import Button, OK, Cancel, RadioButtonGroup, RadioButton

sampleContainer = Container(None, "Test Window", Point(10, 10), 20, 20)

textChild = TextBox(sampleContainer, "Hello", Point(10, 10), 10, 10)
sampleContainer.addChildWindow(textChild)
iterChild = sampleContainer.childIterator()

def sampleValidator(text):
    return True

for i in iterChild:
    print i


try:
    sampleContainer.setFocus()
    sampleContainer.hasFocus()
    sampleContainer.minimize()
    sampleContainer.maximize()
    textChild.setText("")
    textChild.getText()
    textChild.validate(sampleValidator)
except NotImplementedError:
    print "You need to implement this"

sampleAppWindow = AppWindow("Sample App Window")
sampleDialog = DialogBox(sampleAppWindow, "Sample Dialog", Point(10, 10), 20, 20)

try:
    sampleDialog.accept()
    sampleDialog.cancel()
    sampleDialog.getState()
except NotImplementedError:
    print "You need to implement this"

sampleDialog.STATE_ACCEPT
sampleDialog.STATE_CANCEL

rbGroup = RadioButtonGroup(None, "Radio Group", Point(0, 10), 10, 20)
rButton = RadioButton(rbGroup, "Button1", Point(0, 10), 10, 20)
rButton.getState()
rButton.click()
rButton.RADIO_ACTIVE
rButton.RADIO_INACTIVE
