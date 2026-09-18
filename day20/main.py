import time
import turtle as t

from food import Food
from movement import Snake
from score_board import Score

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


food = Food ()
score = Score((-150,270))


game_is_on = True

while game_is_on: 
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.add_score()
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score.reset()
        snake.reset()
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()
       
        

    







































screen.exitonclick()