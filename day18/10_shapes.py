import random
from turtle import Turtle , Screen

mini = Turtle()
mini.shape()

for _ in range (4):   
    mini.right(90)
    mini.forward(100)
mini.backward(50)
for _ in range (6):
    mini.forward(50)
    mini.right(60)
    mini.forward(50)
mini.forward(50)










































screen = Screen()
screen.exitonclick()