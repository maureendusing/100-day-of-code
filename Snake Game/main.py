from turtle import Screen, Turtle 
from turtle import * 

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("blue")
screen.title("Snake")
score = 0 
playing = "True"
turtle_write = Turtle()
turtle_write.hideturtle()
turtle_write.penup()
turtle_write.goto((-40,270))
turtle_write.pendown()
turtle_write.color("white")

turtle_write.write("Score: " + str(score), font=("Arial",20,"normal"))
t1=Turtle(shape="square")
t1.speed("slowest")
t1.color("white")
t1.penup()
t2 =Turtle(shape="square")
t2.color("white")
t2.penup()
t2.goto(0,20)

def up():
    t1.setheading(90)
    t1.forward(20)
def down():
    t1.setheading(270)
    t1.forward(20)
def left():
    t1.setheading(180)
    t1.forward(20)
def right():
    t1.setheading(0)
    t1.forward(20)
def move():
    t1.forward(20)

screen.listen()
screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")

game_playing = True

while game_playing:
    move()
    # if t1.xcor() > 300 or t1.xcor() < -300 or t1.ycor() > 300 or t1.ycor() < -300:
    #     game_playing = False
    #     exit

screen.exitonclick()