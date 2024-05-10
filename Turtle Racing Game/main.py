from turtle import Turtle, Screen 

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)

red = Turtle(shape='turtle')
red.color("red")
red.penup()
red.goto(-225, 40)

orange = Turtle(shape='turtle')
orange.color("orange")
orange.penup()
orange.goto(-225, 20)

yellow = Turtle(shape='turtle')
yellow.color("yellow")
yellow.penup()
yellow.goto(-225, 0)

green = Turtle(shape='turtle')
green.color("green")
green.penup()
green.goto(-225, -20)

blue = Turtle(shape='turtle')
blue.color("blue")
blue.penup()
blue.goto(-225, -40)

purple = Turtle(shape='turtle')
purple.color("yellow")
purple.penup()
purple.goto(-225, -60)

screen.exitonclick()
