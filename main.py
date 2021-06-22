import time
from turtle import  Screen , Turtle

screen = Screen()

screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Python Snake Game!")
#Turn turtle animation on/off and set delay for update drawings.
screen.tracer(0)

start_position =[(0,0),(-20,0),(-40,0)]
parts=[]
for position in start_position:
    part = Turtle("square")
    part.color("white")
    part.penup()
    part.goto(position)
    parts.append(part)


game_is_on=True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    for part_num in range (len(parts)-1,0,-1):
        new_x = parts[part_num-1].xcor()
        new_y=parts [part_num-1].ycor()
        parts[part_num].goto(new_x,new_y)
    parts[0].forward(20)






screen.exitonclick()