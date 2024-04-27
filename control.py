from pynput.mouse import Controller
from pynput.keyboard import Controller
#(left to right,top to bottom)
def control_mouse():
    mouse = Controller()
    mouse.position = (10,500)

def control_keyboard():
    keyboard = Controller()
    keyboard.type("Hello world")

control_keyboard()

