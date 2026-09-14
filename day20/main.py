import turtle as t
from movement import Snake
import time



screen=t.Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

snake = Snake()

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()







































screen.exitonclick()