import random
import turtle as t

screen = t.Screen()
screen.setup(width=500,height=400)
is_race_on = False
guess = screen.textinput(title ="welcome",prompt="choose ur color")
color = ["red","yellow","green","purple","blue","orange"]
y_postions = [-70,-40,-10,20,50,80]
atheletes = []

for _ in range(6):
    mini = t.Turtle(shape="turtle")
    mini.penup()
    mini.goto(-230,y_postions[_])
    mini.color(color[_])
    atheletes.append(mini)

if guess:
    is_race_on = True
    
while is_race_on:
    for turtle in atheletes:
        if turtle.xcor() > 230:
            print(turtle.pencolor())
            is_race_on = False
            if guess == turtle.pencolor():
                print("congrats u won")
            else:
                print("womp womp u lost ") 
        distance = random.randint(0,10)
        turtle.forward(distance)















screen.exitonclick()
