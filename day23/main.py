from turtle import Screen
from chicken import Chicken

screen = Screen()
screen.setup(width = 600 , height = 600)
screen.title("Turtle Race")
screen.tracer(0)

chick = Chicken((0,-280))

screen.listen()
screen.onkey(key = "Up", fun = chick.move_up)
game_is_on = True
while game_is_on:
    screen.update()






















screen.exitonclick()