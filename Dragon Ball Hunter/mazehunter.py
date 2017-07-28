#Maze Runner Game

import turtle as tt
import math
import random as rd

#setup maze area
wn = tt.Screen()
wn.bgcolor("black")
wn.title("Dragon Ball Hunter")
wn.setup(700, 700)
#turn off screen updates
wn.tracer(0) #deals with frames/sec

#register shapes
images = ["player.gif", "onestar_db.gif", "dragon.gif", "db_enemy.gif"]
for image in images:
    tt.register_shape(image)


#pen class to draw which is a turtle
class Pen(tt.Turtle):
    def __init__(self): #refers to the object that the method is being called upon
        tt.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup() #removes the trail left behind by a turtle
        self.speed(0) #animation speed
        
        
#create a player through a class method
class Player(tt.Turtle):
    def __init__(self):
        tt.Turtle.__init__(self)
        self.shape("player.gif")
        #self.color("yellow")
        self.penup()
        self.speed(0)
        self.gold = 0
    
    #player movement
    def go_up(self):
        #calculate the spot to move to
        move_x = self.xcor()
        move_y = self.ycor() + 24
        
        #check is the space has a wall
        if(move_x, move_y) not in walls:
            self.goto(move_x, move_y)
        
    def go_down(self):
        #calculate the spot to move to
        move_x = self.xcor()
        move_y = self.ycor() - 24
        
        #check is the space has a wall
        if(move_x, move_y) not in walls:
            self.goto(move_x, move_y)
            
    def go_right(self):
        #calculate the spot to move to
        move_x = self.xcor() + 24
        move_y = self.ycor()
        
        #check is the space has a wall
        if(move_x, move_y) not in walls:
            self.goto(move_x, move_y)
            
    def go_left(self):
        #calculate the spot to move to
        move_x = self.xcor() - 24
        move_y = self.ycor()
        
        #check is the space has a wall
        if(move_x, move_y) not in walls:
            self.goto(move_x, move_y)
            

    def isCollision(self, other):
        dis = math.sqrt(math.pow(self.xcor() - other.xcor(),2) + math.pow(self.ycor()- other.ycor(),2))
        #checks the distance between the player and goal
        
        if dis < 5:
            return True
        else:
            return False
    #checks if two objects will collide with each other

#create a goal class
class Goal(tt.Turtle):
    def __init__(self, x, y):
        tt.Turtle.__init__(self)
        self.shape("onestar_db.gif")
        #self.color("red")
        self.penup()
        self.speed(0)
        self.gold = 100
        self.goto(x, y)
        
    def hide(self):
        self.goto(2000, 2000)
        self.hideturtle()

#create a enemy class
class Enemy(tt.Turtle):
    def __init__(self, x, y):
        tt.Turtle.__init__(self)
        self.shape("db_enemy.gif")
        #self.color("light salmon")
        self.penup()
        self.speed(0)
        self.gold = 25
        self.goto(x, y)
        self.direction = rd.choice(["up", "down", "left", "right"])
    
    #movement
    def move(self):
        if self.direction == "up":
            dx = 0
            dy = 24
        elif self.direction == "down":
            dx = 0
            dy = -24
        elif self.direction == "left":
            dx = -24
            dy = 0
        elif self.direction == "right":
            dx = 24
            dy = 0
        else:
            dx = 0
            dy = 0
            
        #check if player is close and if sos, move in that direction
        if self.isClose(player):
            if player.xcor() < self.xcor():
                self.direction = "left"
            elif player.xcor() > self.xcor():
                self.direction = "right"
            elif player.ycor() < self.ycor():
                self.direction = "down"
            elif player.ycor() > self.ycor():
                self.direction = "up"
        
        #calculate the spot to move to
        move_x = self.xcor() + dx
        move_y = self.ycor() + dy
        
        #check is the space has a wall
        if(move_x, move_y) not in walls:
            self.goto(move_x, move_y)
        else:
            #choose different direction
            self.direction = rd.choice(["up", "down", "left", "right"])
            
        #set timer for next movement
        tt.ontimer(self.move, t = rd.randint(100, 300))
        
    def isClose(self, other):
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        dis = math.sqrt((a**2) + (b**2))
        
        if dis < 75:
            return True
        else:
            return False
        
    def hide(self):
        self.goto(2000, 2000)
        self.hideturtle()
        
            
#create levels list
levels = [""] # "" adds level_0 to the list so there is no confusion in numbering

#first level
level_1 = [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XP XXXXXXXE         XXXXX",
"X  XXXXXXX  XXXXXX  XXXXX",
"X       XX  XXXXXX  XXXXX",
"X       XX  XXX       XXX",
"XXXXXX  XX  XXX       XXX",
"XXXXXX  XX  XXXXXX  XXXXX",
"XXXXXX  XX    XXXX  XXXXX",
"X  XXX        XXXXG XXXXX",
"X  XXX  XXXXXXXXXXXXXXXXX",
"X        XXXXXXXXXXXXXXXX",
"XE               XXXXXXXX",
"XXXXXXXXXXXX     XXXXX  X",
"XXXXXXXXXXXXXXX  XXXXX  X",
"XXX  XXXXXXXXXX         X",
"XXX                     X",
"XXX  E      XXXXXXXXXXXXX",
"XXXXXXXXXX  XXXXXXXXXXXXX",
"XXXXXXXXXX              X",
"XX   XXXXX              X",
"XX   XXXXXXXXXXXXX  XXXXX",
"XX    XXXXXXXXXXX   XXXXX",
"XX          XXXX        X",
"XXXX            E       X",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
]

#level 2
level_2 = [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"X  XXXXXXXE         XXXXX",
"X  XXXXXXX  XXXXXX  XXXXX",
"X       XX  XXXXXXXXXXXXX",
"X                     XXX",
"XXXXXX  XX  XXXXXXX   XXX",
"XXXXXX  XX  XXXXXX  XXXXX",
"XXXXXX  XX    XXXX  XXXXX",
"X GXXX        X     XXXXX",
"X XXXX X XXXXXXX XXXXXXXX",
"X        XXXXX   XXXXXXXX",
"XE         XX    XXXXXXXX",
"XXXXXXXXXXXX       XXX  X",
"XXXXXXXXXXXXXXX    XXX  X",
"XXX  XXXXXXXXXX X       X",
"XXX             X       X",
"XXX  E      XXXXX   XXXXX",
"XXXXXXXXXXXXXXXXXX   XXXX",
"XXXXXXXXXX X  XX        X",
"XX   XXXXX              X",
"XXP  XXXXXXXXXXXXX XXXXXX",
"XX    XXXXXXXXXXX   XXXXX",
"XX          XXXX        X",
"XXXX                    X",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
]

#add goal list
goals = []

#add enemies list
enemies = []

#create wall coordinates
walls = []

#add level to levels list
levels.append(level_1)
levels.append(level_2)

#level setup function
def setup_maze(level):
    for y in range(len(level)): #how many rows we have(0-24)
        for x in range(len(level[y])): #how many columns we have(0-24)
            #get the character at each x, y coordinate
            #we get row first then column
            character = level[y][x]
            #calculaate the mazes x, y coordinates
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)
            
            #check if it is a wall (repersented by X)
            if(character == "X"):
                pen.goto(screen_x, screen_y)
                pen.shape("dragon.gif")
                pen.stamp() #puts a block on the screen and leaves it there
                #add wall coordinates to walls list
                walls.append((screen_x, screen_y))
                                
            #check if it is a player (repersented by P)
            if character == "P":
                player.goto(screen_x, screen_y)
            
            #check if it is a goal (repersented by G)
            if character == "G":
                goals.append(Goal(screen_x, screen_y))
            
            #check if it is an enemy (repersented by E)
            if character == "E":
                enemies.append(Enemy(screen_x, screen_y))

#create a class instance
pen = Pen()
player = Player()

#setup the level
setup_maze(levels[1])

#keyboard bindings
tt.listen() #tells the program to look for key presses
tt.onkey(player.go_left, "Left") 
tt.onkey(player.go_right, "Right") 
tt.onkey(player.go_up, "Up")
tt.onkey(player.go_down, "Down") 

#turn off screen updates
wn.tracer(0) #deals with frames/sec

#start moving enemies
for enemy in enemies:
    tt.ontimer(enemy.move, t = 250)

#main game loop
while(True):
    
    #check for collision between player and goal
    #iterate through goals list
    for goal in goals:
        if player.isCollision(goal):
            #add the gold from goal to player
            player.gold += goal.gold
            print("Player Gold: {}".format(player.gold))
            #hide the goal
            goal.hide()
            #remove goal from goals list
            goals.remove(goal)
            #setup_maze(levels[2])
    
    #iterate through the enemy list to see if the player collides
    for enemy in enemies:
        if player.isCollision(enemy):
            print("Player has been killed!")
            player.gold -= enemy.gold
            print("Player Gold: {}".format(player.gold)) 
            #setup_maze(levels[1])
    
    #update screen
    wn.update()
    
    
    
    
    
    
    