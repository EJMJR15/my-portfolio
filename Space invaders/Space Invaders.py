from dis import Instruction
import re
import turtle as trtl
import random as rand
import time
wn = trtl.Screen()
#restart
restart = trtl.Turtle()
restart.hideturtle()
restart.penup()
restart.goto(0,30)
wn.addshape("reastart.gif")
restart_image = "reastart.gif"
def draw_restart(active_startbutton):
  restart.shape(restart_image)
  wn.update()
draw_restart(restart_image)
#-------------------
score_num = 0
score= trtl.Turtle()
score.color("White")
score.penup()
score.hideturtle()
score.goto(-300,-400)
score.write("Score = " + str(score_num), font=("Arial", 30, "bold"))
#bg
 
bg_pic = "bgpic.gif"
wn.bgpic(bg_pic)
wn.update()
#Instructions
words = """
                    Your goal is to shoot the Invaders above.
You can do this by moving your ship left or right with the arrow keys.
                                     Press space to shoot.
                                     Click Start to Begin
"""
start= trtl.Turtle()
#start.hideturtle()
#start.shape("rectangle")
start.shapesize(5)
start.penup()
start.color("White")
start.goto(0,30)



#button image

wn.addshape("startbutton.gif")
startbutton_image = "startbutton.gif"
def draw_startbutton(active_startbutton):
  start.shape(startbutton_image)
  wn.update()
draw_startbutton(startbutton_image)

instruction=trtl.Turtle()
instruction.hideturtle()
instruction.penup()
instruction.color("White")
instruction.goto(-200,-80)
instruction.write(words, font=("Arial", 10, "bold"))
# Lives~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
lives = 0


live1 = trtl.Turtle()
live1.penup()
live1.speed(0)
live1.goto(90,-400)
#live 1 pic
wn.addshape("spaceship.gif")
spaceship_image = "spaceship.gif"
 
def draw_spaceship(active_spaceship):
  live1.shape(spaceship_image)
  wn.update()
draw_spaceship(spaceship_image)
live2 = trtl.Turtle()
live2.penup()
live2.speed(0)
live2.goto(150,-400)
#live 2 pic
wn.addshape("spaceship.gif")
spaceship_image = "spaceship.gif"
 
def draw_spaceship(active_spaceship):
  live2.shape(spaceship_image)
  wn.update()
draw_spaceship(spaceship_image)
live3 = trtl.Turtle()
live3.penup()
live3.speed(0)
live3.goto(210,-400)
#live 3 pic
wn.addshape("spaceship.gif")
spaceship_image = "spaceship.gif"
 
def draw_spaceship(active_spaceship):
  live3.shape(spaceship_image)
  wn.update()
draw_spaceship(spaceship_image)
play_game = False
#painter
painter = trtl.Turtle()
painter.hideturtle()
painter.color("White")
painter.speed(0)
painter.penup()
painter.goto(-310,400)
painter.right(90)
painter.pendown()
painter.goto(-310,-330)
painter.goto(310,-330)
painter.goto(310,400)
painter.goto(-310,400)
#Spaceship
spaceship = trtl.Turtle()
spaceship.penup()
spaceship.speed(0)
spaceship.hideturtle()
spaceship.goto(0,-300)
spaceship.left(90)
space_x = spaceship.xcor()

#spaceship pic
wn.addshape("spaceship.gif")
spaceship_image = "spaceship.gif"
 
def draw_spaceship(active_spaceship):
  spaceship.shape(spaceship_image)
  wn.update()
draw_spaceship(spaceship_image)
#bullet
bullet= trtl.Turtle()
bullet.hideturtle()
bullet.left(90)
bullet.penup()
bullet.speed(0)
bullet.goto(0,402)
space_x = spaceship.xcor()
space_y = spaceship.ycor()
bullet_y = bullet.ycor()
bullet_on = False

#bullet image
wn.addshape("bullet.gif")
bullet_image = "bullet.gif"
def draw_bullet(active_bullet):
  bullet.shape(bullet_image)
  wn.update()
draw_bullet(bullet_image)
 
#Invader1~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
invader_speed = 5
invader1 = trtl.Turtle()
invader1.penup()
invader1.hideturtle()
invader1.goto(-280,380)
invader1.speed(0)
invader1_x = invader1.xcor()
invader1_y = invader1.ycor()
invader1.shape("circle")
invader1.shapesize(2)
invader1.color("Blue")
#invader image
wn.addshape("spaceinvader.gif")
invader_image = "spaceinvader.gif"
def draw_invader(active_invader):
  invader1.shape(invader_image)
  wn.update()
draw_invader(invader_image)
 
#Invader2~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
invader2 = trtl.Turtle()
invader2.penup()
invader2.hideturtle()
invader2.goto(-230,380)
invader2.speed(0)
invader2_x = invader2.xcor()
invader2_y = invader2.ycor()
invader2.shape("circle")
invader2.shapesize(2)
invader2.color("Red")
#invader image
wn.addshape("spaceinvader.gif")
invader_image = "spaceinvader.gif"
def draw_invader(active_invader):
  invader2.shape(invader_image)
  wn.update()
draw_invader(invader_image)
 
#Invader3~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
invader3 = trtl.Turtle()
invader3.penup()
invader3.hideturtle()
invader3.goto(280,380)
invader3.speed(0)
invader3_x = invader3.xcor()
invader3_y = invader3.ycor()
invader3.setheading(180)
invader3.shape("circle")
invader3.shapesize(2)
invader3.color("Green")
#invader image
wn.addshape("spaceinvader.gif")
invader_image = "spaceinvader.gif"
def draw_invader(active_invader):
  invader3.shape(invader_image)
  wn.update()
draw_invader(invader_image)
 
#Invader4~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
invader4 = trtl.Turtle()
invader4.penup()
invader4.hideturtle()
invader4.goto(230,380)
invader4.speed(0)
invader4_x = invader4.xcor()
invader4_y = invader4.ycor()
invader4.setheading(180)
invader4.shape("circle")
invader4.shapesize(2)
invader4.color("Black")
#invader image
wn.addshape("spaceinvader.gif")
invader_image = "spaceinvader.gif"
def draw_invader(active_invader):
  invader4.shape(invader_image)
  wn.update()
draw_invader(invader_image)
 
#wn.bcpic()
def shoot():
    global bullet_on
    space_x = spaceship.xcor()
    bullet.speed(0)
    bullet.goto(space_x+2,-265)
    bullet.speed(0)
    bullet.showturtle()
    bullet_on = True
def reset_shoot():
    global bullet_on
    bullet_on = False
    space_x = spaceship.xcor()
    bullet.hideturtle()
    bullet.speed(0)
    bullet.goto(space_x,-320)
def left():
    current_x = spaceship.xcor()
    current_y = spaceship.ycor()
    if current_x <= -300:
        spaceship.goto(-300,current_y)
    else:
        current_x -= 10
        spaceship.goto(current_x,current_y)
def right():
    current_x = spaceship.xcor()
    current_y = spaceship.ycor()
    if current_x >= 300:
        spaceship.goto(300,current_y)
    else:
        current_x += 10
        spaceship.goto(current_x,current_y)
gameover = trtl.Turtle()
def game_over():
  
    bullet.hideturtle()
    spaceship.hideturtle()
    gameover.penup()
    gameover.goto(-20,-50)
    gameover.color("White")
    gameover.write("GAME OVER", font=("Arial", 30,"bold"))
    restart.showturtle()

def start_game(x,y):
    global play_game
    gameover.hideturtle()
    restart.hideturtle()
    play_game = True
    start.hideturtle()
    instruction.hideturtle()
    start.clear()
    instruction.clear()
    


    
def invader_restart():
    global lives
    global play_game
    invader1.hideturtle()
    invader2.hideturtle()
    invader3.hideturtle()
    invader4.hideturtle()
    invader1.goto(-280,380)
    invader2.goto(-230,380)
    invader3.setheading(180)
    invader3.goto(280,380)
    invader4.setheading(180)
    invader4.goto(230,380)
    if lives == 3:
        live1.hideturtle()
        lives -=1
    elif lives == 2:   
        live2.hideturtle()
        lives -=1
    elif lives == 1:
        live3.hideturtle()
        lives -=1
def reset_lives():
    lives += 3
    live1.showturtle()
    live2.showturtle()
    live3.showturtle()
    
    if lives == 0:
        play_game = False
        game_over()
        reset_lives()



while play_game == False:
    start.onclick(start_game)
    restart.onclick(start_game)
#Runs Everything
while play_game == True:
    
    spaceship.showturtle()
    
    invader1.showturtle()
    invader2.showturtle()
    invader3.showturtle()
    invader4.showturtle()
    spaceship.showturtle()
    if bullet_on == True:
        bullet.forward(20)
    bullet_y = bullet.ycor()
    if bullet_y >= 401:
        reset_shoot()
 
    wn.onkeypress(shoot, "space")
    wn.onkeypress(left, "Left")
    wn.onkeypress(right, "Right")
    wn.listen()
    #Invader 1
    invader_y = invader1.ycor()
    invader_x = invader1.xcor()
    invader1.forward(invader_speed)
    if invader_x >= 290 and invader_x <= 310:
        invader1.setheading(270)
        invader1.forward(30)
        invader1.setheading(180)
    if invader_x <=-290 and invader_x <=-310:      
        invader1.setheading(270)
        invader1.forward(20)
        invader1.setheading(0)
    #Invader 2
    invader2_y = invader2.ycor()
    invader2_x = invader2.xcor()
    invader2.forward(invader_speed)
    if invader2_x >= 290 and invader2_x <= 310:
        invader2.setheading(270)
        invader2.forward(30)
        invader2.setheading(180)
    if invader2_x <=-290 and invader2_x <=-310:      
        invader2.setheading(270)
        invader2.forward(30)
        invader2.setheading(0)
    #Invader 3
    invader3_y = invader3.ycor()
    invader3_x = invader3.xcor()
    invader3.forward(invader_speed)
    if invader3_x >= 290 and invader3_x <= 310:
        invader3.setheading(270)
        invader3.forward(50)
        invader3.setheading(180)
    if invader3_x <=-290 and invader3_x <=-310:      
        invader3.setheading(270)
        invader3.forward(35)
        invader3.setheading(0)
    #Invader 4
    invader4_y = invader4.ycor()
    invader4_x = invader4.xcor()
    invader4.forward(invader_speed)
    if invader4_x >= 290 and invader4_x <= 310:
        invader4.setheading(270)
        invader4.forward(50)
        invader4.setheading(180)
    if invader4_x <=-290 and invader4_x <=-310:      
        invader4.setheading(270)
        invader4.forward(40)
        invader4.setheading(0)
    # Colision Bettwen bullets and invaders
    invader_y = invader1.ycor()
    invader_x = invader1.xcor()
    bullet_x = bullet.xcor()
    bullet_y = bullet.ycor()
    if abs(invader_x - bullet_x) <= 20 and abs(invader_y - bullet_y) <= 20:
        invader1.hideturtle()
        score_num += 100
        score.clear()
        score.write("Score = " + str(score_num), font=("Arial", 30, "bold"))
        reset_shoot()
        invader1.goto(-280,380)
    #Invader 2~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    invader2_y = invader2.ycor()
    invader2_x = invader2.xcor()
    bullet_x = bullet.xcor()
    bullet_y = bullet.ycor()
    if abs(invader2_x - bullet_x) <= 20 and abs(invader2_y - bullet_y) <= 20:
        invader2.hideturtle()
        score_num += 100
        score.clear()
        score.write("Score = " + str(score_num), font=("Arial", 30, "bold"))
        reset_shoot()
        invader2.goto(-230,380)
    #Invader 3~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    invader3_y = invader3.ycor()
    invader3_x = invader3.xcor()
    bullet_x = bullet.xcor()
    bullet_y = bullet.ycor()
    if abs(invader3_x - bullet_x) <= 20 and abs(invader3_y - bullet_y) <= 20:
        invader3.hideturtle()
        score_num += 100
        score.clear()
        score.write("Score = " + str(score_num), font=("Arial", 30, "bold"))
        reset_shoot()
        invader3.setheading(180)
        invader3.goto(280,380)
    #Invader 4~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    invader4_y = invader4.ycor()
    invader4_x = invader4.xcor()
    bullet_x = bullet.xcor()
    bullet_y = bullet.ycor()
    if abs(invader4_x - bullet_x) <= 20 and abs(invader4_y - bullet_y) <= 20:
        invader4.hideturtle()
        score_num += 100
        score.clear()
        score.write("Score = " + str(score_num), font=("Arial", 30, "bold"))
        reset_shoot()
        invader4.setheading(180)
        invader4.goto(230,380)
    #invaders 1-4 and spaceship~~~~~~~~~~~~~~~~~~~~~~~~
    invader1_y = invader1.ycor()
    spaceship_y = spaceship.ycor()
    if abs(invader1_y - spaceship_y) <= 20:
        invader_restart()
    invader2_y = invader2.ycor()
    spaceship_y = spaceship.ycor()
    if abs(invader2_y - spaceship_y) <= 20:
        invader_restart()
    invader3_y = invader3.ycor()
    spaceship_y = spaceship.ycor()
    if abs(invader3_y - spaceship_y) <= 20:
        invader_restart()
    invader4_y = invader4.ycor()
    spaceship_y = spaceship.ycor()
    if abs(invader4_y - spaceship_y) <= 20:
        invader_restart()
    #Invader Speed~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    if score_num == 500:
        invader_speed = 8
    if score_num == 1000:
        invader_speed = 9
    if score_num == 1500:
        invader_speed = 10
    if score_num == 2000:
        invader_speed = 10.5
    if score_num == 3000:
        invader_speed = 11
wn.mainloop()