import turtle as t
from movement import Snake
from food import Food
import time
import random



screen=t.Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

snake = Snake()
screen.listen()
screen.onkey(key = "Up",fun = snake.move_up)
screen.onkey(key = "Down",fun= snake.move_down)
screen.onkey(key= "Left",fun = snake.move_left)
screen.onkey(key="Right",fun=snake.move_right)


x_pos = random.randint(-290,290)
y_pos = random.randint(-290,290)
food = Food()
food.appear(x_pos,y_pos)

game_is_on = True

while game_is_on:
  
    screen.update()
    time.sleep(0.1)
    snake.move()
    







































screen.exitonclick()