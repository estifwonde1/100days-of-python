from turtle import Screen
from chicken import Chicken
from obstacle import Obstacle
import random
import time

colors = ["hotpink", "darkorange", "gold", "forestgreen", "skyblue", 
          "turquoise", "royalblue", "purple", "crimson", "darkorchid"]
screen = Screen()
screen.setup(width = 600 , height = 600)
screen.title("Turtle Race")
screen.tracer(0)

chick = Chicken((0,-280))
rand_num = random.randrange(-300,301,20)
color = random.choice(colors)
obstacle = Obstacle((300,rand_num),color)

screen.listen()
screen.onkey(key = "Up", fun = chick.move_up)
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    obstacle.move()






















screen.exitonclick()