#Turtle Graphics Game

import turtle as tt
import math 
import random
import os
import winsound

#set up the playing screen
wn = tt.Screen()
wn.bgcolor("white")
wn.bgpic("backimg.gif")
#tracer drops frames for better looking animations
wn.tracer(2)

#border dimensions
myPen = tt.Turtle()
myPen.penup()
myPen.setposition(-300,-300)
myPen.pendown()
myPen.pensize(3)
for side in range(4):
    myPen.forward(600)
    myPen.left(90)
myPen.hideturtle()

#create player turtle
player = tt.Turtle()
player.color("red")
player.shape("turtle")
#removes the turtles trail
player.penup()
#animation speed
player.speed(0)

#create multiple goals
maxGoals = 6
goals = []
for count in range(maxGoals):
    #create goals
    goals.append(tt.Turtle())
    goals[count].color("black")
    goals[count].shape("circle")
    goals[count].penup()
    goals[count].speed(0)
    goals[count].setposition(random.randint(-300, 300), random.randint(-300, 300))

#create a score variable
score = 0

#speed variable
speed = 1

#functions
def turnleft():
    player.left(15)
#turns player 15 degrees left

def turnright():
    player.right(15)
#turns player 15 degrees right

def incspeed():
    global speed
    speed += 1
#increases player speed by one
    
def decspeed():
    global speed
    speed -= 1
#decreases player speed by one

def isCollision(t1, t2):
    dis = math.sqrt(math.pow(t1.xcor() - t2.xcor(),2) + math.pow(t1.ycor()- t2.ycor(),2))
    #checks the distance between the player and goal
    if dis < 20:
        return True
    else:
        return False
#checks if two objects will collide with each other
        
    
def boundary(b1):
    if b1.xcor() > 290 or b1.xcor() < -290:
        b1.right(180)
        #winsound.Beep(300,100)
        #os.system("afplay bounce.mp3&")#'&' symbol makes sure the game continues to play
    elif b1.ycor() > 290 or b1.ycor() < -290:
        b1.right(180)
        #winsound.Beep(300,100)
        #os.system("afplay bounce.mp3&")#'&' symbol makes sure the game continues to play; only works for mac and linux
#restricts objects to the set boundary

'''move the turtle'''
#keyboard bindings
tt.listen() #tells the program to look for key presses
tt.onkey(turnleft, "Left") 
tt.onkey(turnright, "Right") 
tt.onkey(incspeed, "Up")
tt.onkey(decspeed, "Down") 


while(True):
    player.forward(speed)
    
    #boundary check
    boundary(player)
    for count in range(maxGoals):
        boundary(goals[count])

   
    #move goals
    for count in range(maxGoals):
        goals[count].forward(1)
        
        #collision cheching and repostioning the goal to a random position & angle
        if isCollision(player, goals[count]):
            goals[count].setposition(random.randint(-300, 300), random.randint(-300, 300))
            goals[count].right(random.randint(0,360))
            score += 1
            
            #draw score on play screen
            myPen.undo() #erases previous score
            myPen.penup()
            myPen.hideturtle()
            myPen.setposition(-290, 310)
            scorestring = "Score: %s" %score
            myPen.write(scorestring, False, align = "left", font =("Arial", 14, "normal"))



delay = input("Press enter to end....")