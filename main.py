from turtle import  Screen , Turtle

screen = Screen()

screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Python Snake Game!")

start_position =[(0,0),(-20,0),(-40,0)]
for position in start_position:
    part = Turtle("square")
    part.color("white")
    part.goto(position)



screen.exitonclick()