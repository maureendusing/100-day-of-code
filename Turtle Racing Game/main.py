from tkinter import Button, Label, Toplevel
from turtle import Turtle, Screen 
import random

#known issue: UI -> Winner printing, dropdown input 

screen = Screen()
racing = False
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

for index in range(0,6): 
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[index])
    new_turtle.goto(-225, 60-(index+1)*20)
    turtles.append(new_turtle)

if user_bet: 
    racing = True

while racing: 
    for turtle in turtles: 
        distance = random.randint(0,10)
        turtle.forward(distance)
        if turtle.xcor() > 230:
            racing = False
            winning_turtle = turtle.pencolor()

turtle_write= Turtle()
turtle_write.penup()
turtle_write.goto(-200,150)
turtle_write.write(f"winner was {winning_turtle}")
if winning_turtle == user_bet:
    print("YOU WON!")
else: 
    print("YOU LOST :(")

screen.exitonclick()
