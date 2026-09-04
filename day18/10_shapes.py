import random
from turtle import Turtle, Screen

mini = Turtle()
mini.shape()
colors = ["crimson","darkorange","gold","forestgreen","darkcyan","deepskyblue","royalblue","hotpink","saddlebrown"]
num = len(colors)
def randoming():
    pick = random.randint(0,num-1)
    randomize = colors[pick]
    mini.color(randomize)

def draw_shape(num_sides):
    angle = 360/num_sides
    for _ in range(num_sides):    
        mini.forward(100)
        mini.right(angle)
for _ in range(3,13):
    draw_shape(_)
    randoming()

#refactoring it and will continue tommorrow


    





screen = Screen()
screen.exitonclick()
