import turtle as t
import random


screen = t.Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("snakey cake")
food = t.Turtle("circle")
food.color("green")
food.shapesize(0.5,0.5)
food.penup()
food.goto(40,40)
segement_postions = [(0,0),(-20,0),(-40,0)]
fully = []
for _ in segement_postions:
    snakey = t.Turtle(shape = "square")
    snakey.color("white")
    snakey.penup()
    snakey.goto(_)
    fully.append(snakey)
is_gameover = True
while is_gameover:
    snakey.penup()
    snakey.forward(10)
    snakey.speed(1)
    for snake in fully:
        if snake.xcor() > 280 or snake.xcor() < -280 or snake.ycor() > 280 or snake.ycor() < -280:
            is_gameover = False
        def move_right():
            new_heading = snake.heading() + 90
            snake.setheading(new_heading)
        def move_left():
            new_heading = snake.heading() - 90
            snake.setheading(new_heading)

    screen.listen()
    screen.onkey(key ="d",fun = move_right)
    screen.onkey(key = "a",fun = move_left)
    














screen.exitonclick()