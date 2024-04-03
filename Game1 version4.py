# Turtle Graphics Game – Space Turtle Chomp
import turtle
import math
import random
import winsound
import time

turtle.setup(650,650)
wn=turtle.Screen()
wn.bgcolor('plum')
wn.bgpic('kbgame-bg.gif')
wn.tracer(3)

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
score = 0
# Penup Turtle shape won't leave a line 
player.penup()
player.speed(0)

# Create opponent turtle
comp = turtle.Turtle()
comp.color('red')
comp.shape('turtle')
comp.penup()
comp.setposition(random.randint(-290, 290), random.randint(-290, 290))

# Create competition score
comp_score = 0
mypen2 = turtle.Turtle()
mypen2.color('red')
mypen2.hideturtle()

# Create food
maxFoods = 10
foods=[]
for count in range(maxFoods):
    food=turtle.Turtle()
    food.color('lightgreen')
    food.shape('circle')
    food.shapesize(0.5)
    food.penup()
    food.speed(0)
    food.setposition(random.randint(-290,290),random.randint(-290,290))
    foods.append(food)

speed = 1
# Set game time limit for 1 minute (60 seconds)
timeout = time.time() + 10*6

# Function defintion

def turn_left():
    player.left(90)
def turn_right():
    player.right(90)
def increase_speed():
    global speed 
    speed+=1

def isCollision(t1, t2):
       d = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2) + math.pow(t1.ycor()-t2.ycor(),2))
       if d < 20:
           return True
       else:
           return False

#Keyboard stroke mapping
turtle.listen()
turtle.onkey(turn_left, 'Left')
turtle.onkey(turn_right,'Right')
turtle.onkey(increase_speed,'Up')

# Turtle movement
while True:
    gametime = 0
    if gametime==6  or time.time()>timeout:
        break
    gametime = gametime+1

    player.forward(speed)
    comp.forward(12)
# Boundary Player Checking x & y coordinate
    if player.xcor() > 290 or player.xcor() < -290:
       player.right(180)
       winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)
    if player.ycor() >290 or player.ycor()< -290:
        player.right(180)
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)
 # Boundary Comp Checking x & y coordinate
    if comp.xcor() > 290 or comp.xcor() < -290:
       comp.right(180)
       winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)
    if comp.ycor() >290 or comp.ycor()< -290:
        comp.right(180)
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)
   
# Food movement
    for food in foods:
        food.forward(3) 
        # Boundary Food Checking x & y coordinate
        if food.xcor() > 290 or food.xcor() < -290:
            food.right(random.randint(0,360))
            winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)
        if food.ycor() >290 or food.ycor()< -290:
            food.right(random.randint(0,360))
            winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)
        if isCollision(player,food):
            food.setposition(random.randint(-290,290),random.randint(-290,290))
            food.right(random.randint(0,360))
            winsound.PlaySound('chomp.wav', winsound.SND_ASYNC)
            score +=1
            # Draw the score on the screen
            mypen.undo()
            mypen.penup()
            mypen.hideturtle()
            mypen.setposition(-290, 310)
            scorestring ="Score: %s" % score
            mypen.write(scorestring, False, align='left', font=('Arial', 14, 'normal'))

        if isCollision(comp, food):
            food.setposition(random.randint(-290, 290), random.randint(-290, 290))
            food.right(random.randint(0,360))
            winsound.PlaySound('chomp.wav', winsound.SND_ASYNC)
            comp_score +=1
            mypen2.undo()
            mypen2.penup()
            mypen2.hideturtle()
            mypen2.setposition(200, 305)
            scorestring ="Score: %s" % comp_score
            mypen2.write(scorestring, False, align='left', font=('Arial', 14, 'normal'))

if (int(score) > int(comp_score)):
    mypen.setposition(0, 0)
    mypen.color("yellow")
    mypen.write("Game Over: You WIN", False, align="center", font=("Arial", 28, "normal"))
else:
    mypen.setposition(0, 0)
    mypen.color("yellow")
    mypen.write("Game Over: You LOSE", False, align="center", font=("Arial", 28, "normal"))

delay = input("Press Enter to finish.")