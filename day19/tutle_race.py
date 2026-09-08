import random
import turtle as t
screen = t.Screen()
screen.setup(width=500,height=400)
guess = screen.textinput(title ="welcome",prompt="choose ur color")
print(guess)

def race(color): 
    distance = random.randint(0,10)
    color.forward(distance)

n = -230
green = t.Turtle()
green.shape("turtle")
green.color("green")
green.penup()
green.goto(n,-30)
purple= t.Turtle()
purple.shape("turtle")
purple.color("purple")
purple.penup()
purple.goto(n,-60)
blue = t.Turtle()
blue.shape("turtle")
blue.color("blue")
blue.penup()
blue.goto(n,-90)
yellow =t.Turtle()
yellow.shape("turtle")
yellow.color("yellow")
yellow.penup()
yellow.goto(n,0)
orange = t.Turtle()
orange.shape("turtle")
orange.color("orange")
orange.penup()
orange.goto(n,30)
red = t.Turtle()
red.shape("turtle")
red.color("red")
red.penup()
red.goto(n,60)
for _ in range (90):
    race(green)
    race(purple)
    race(blue)
    race(yellow)
    race(orange)
    race(red)












screen.exitonclick()