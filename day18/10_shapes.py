import random
from turtle import Turtle, Screen

mini = Turtle()
mini.shape()
colors = ["crimson","darkorange","gold","forestgreen","darkcyan","deepskyblue","royalblue","darkorchild","hotpink","saddlebrown"]
num = len(colors)

degrees = [120,90,72,60,51.43,45,40,36,32.73,30]
ro = True
while ro:
    pick = random.randint(0,num-1)
    randomize = colors[pick]
#will continue from here tommorrow
    for _ in range (3):
        mini.color(randomize)
        mini.right(120)
        mini.forward(100)
    for _ in range (4):
        mini.right(90)
        mini.forward(100)
    mini.backward(100)
    for _ in range (5):
        mini.forward(100)
        mini.right(72)
    mini.forward(100)
    for _ in range(6):
        mini.right(60)
        mini.forward(100)
    for _ in range(7):
        mini.right(51.43)
        mini.forward(100)
    for _ in range(8):
        mini.right(45)
        mini.forward(100)
    for _ in range(9):
        mini.right(40)
        mini.forward(100)
    for _ in range (10):
        mini.right(36)
        mini.forward(100)
    for _ in range (11):
        mini.right(32.73)
        mini.forward(100)
    for _ in range (12):
        mini.right(30)
        mini.forward(100)

    





screen = Screen()
screen.exitonclick()
