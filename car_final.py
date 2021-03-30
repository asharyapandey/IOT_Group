from gpiozero import Robot
from bluedot import BlueDot



right =(16,26)
left = (20,19)
rob = Robot(left=left, right=right)
bd = BlueDot()

def move(pos):
    if pos.top:
        rob.forward(1)
    elif pos.bottom:
        rob.backward(1)
    elif pos.left:
        rob.left(0.25)
    elif pos.right:
        rob.right(0.25)

def stop():
    rob.stop()

bd.when_pressed = move
bd.when_moved = move
bd.when_released = stop
