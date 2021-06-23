import time
from turtle import  Screen

from scoreboard import Scoreboard
from snake import Snake
from snake_food import Food

screen = Screen()

screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Python Snake Game!")
#Turn turtle animation on/off and set delay for update drawings.
screen.tracer(0)

snake = Snake()
snake_food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")

game_is_on=True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()
    # detect food collision
    if snake.head.distance(snake_food)<15:
        snake_food.refresh_location()

screen.exitonclick()