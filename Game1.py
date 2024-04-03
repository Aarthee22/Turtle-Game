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
speed = 1
while True:
    player.forward(speed)