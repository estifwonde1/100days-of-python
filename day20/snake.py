import random
import turtle as t


screen = t.Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("snakey cake ")
segement_postions = [(0,0),(-20,0),(-40,0)]

size = []
for _ in segement_postions:
    snakey = t.Turtle(shape = "square")
    snakey.color("white")
    snakey.goto(_)
    




















screen.exitonclick()