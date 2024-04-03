# Turtle Graphics Game – Space Turtle Chomp
import turtle
turtle.setup(650,650)
wn=turtle.Screen()
wn.bgcolor('plum')
# Create player turtle
player=turtle.Turtle()
player.color('darkorange')
player.shape('square')
# Penup Turtle shape won't leave a line 
player.penup()
player.speed(0)
speed = 1
def turn_left():
    player.left(90)
def turn_right():
    player.right(90)
def increase_speed():
    global speed 
    speed+=1
turtle.listen()
turtle.onkey(turn_left, 'Left')
turtle.onkey(turn_right,'Right')
turtle.onkey(increase_speed,'Up')
while True:
    player.forward(speed)