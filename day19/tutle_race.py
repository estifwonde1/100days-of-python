import random
import turtle as t
screen = t.Screen()
screen.setup(width=500,height=400)
guess = screen.textinput(title ="welcome",prompt="choose ur color")
print(guess)
color = ["red","yellow","green","purple","blue","orange"]
y_postions = [-70,-40,-10,20,50,80]

def race(color): 
    distance = random.randint(0,10)
    color.forward(distance)

n = -230
for _ in range(6):
    mini = t.Turtle(shape="turtle")
    mini.penup()
    mini.goto(n,y_postions[_])
    mini.color(color[_])














screen.exitonclick()