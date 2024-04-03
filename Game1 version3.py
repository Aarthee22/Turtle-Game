# Turtle Graphics Game – Space Turtle Chomp
import turtle
import math
import random

turtle.setup(650,650)
wn=turtle.Screen()
wn.bgcolor('plum')

# Draw border
mypen = turtle.Turtle()
mypen.penup()
mypen.setposition(-300,-300)
mypen.pendown()
mypen.pensize(6)
mypen.color('white')
for side in range(4):
    mypen.forward(600)
    mypen.left(90)
mypen.hideturtle()

# Create player turtle
player=turtle.Turtle()
player.color('darkorange')
player.shape('square')

# Penup Turtle shape won't leave a line 
player.penup()
player.speed(0)

# Create food
food=turtle.Turtle()
food.color('lightgreen')
food.shape('circle')
food.penup()
food.speed(0)
food.setposition(-100,100)

speed = 1
# Function defintion

def turn_left():
    player.left(90)
def turn_right():
    player.right(90)
def increase_speed():
    global speed 
    speed+=1

#Keyboard stroke mapping
turtle.listen()
turtle.onkey(turn_left, 'Left')
turtle.onkey(turn_right,'Right')
turtle.onkey(increase_speed,'Up')

# Turtle movement
while True:
    player.forward(speed)
    d=math.sqrt(math.pow(player.xcor()-food.xcor(),2)+math.pow(player.ycor()-food.ycor(),2))
    if d<20:
        food.setposition(random.randint(-290,290),random.randint(-290,290))

# Boundary Player Checking x coordinate
    if player.xcor() > 290 or player.xcor() < -290:
       player.right(180)
    if player.ycor() >290 or player.ycor()< -290:
        player.right(180)
