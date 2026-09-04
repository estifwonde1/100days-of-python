from turtle import Screen, Turtle
from shapes import randoming
import random
mini = Turtle()
randoming()

num_walks = 10
for _ in range(num_walks):
    mini.forward(20)




screen = Screen()
screen.exitonclick()
