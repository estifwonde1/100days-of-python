from turtle import Screen
from chicken import Chicken
from obstacle import Obstacle
from score_board import Score
import random
import time

colors = ["hotpink", "darkorange", "gold", "forestgreen", "skyblue", 
          "turquoise", "royalblue", "purple", "crimson", "darkorchid"]
screen = Screen()
screen.setup(width = 600 , height = 600)
screen.title("Turtle Race")
screen.tracer(0)

chick = Chicken((0,-280))
level = Score((-290,270))
    
hold = []
screen.listen()
screen.onkey(key = "Up", fun = chick.move_up)
game_is_on = True
inc = 0.3
while game_is_on:
    screen.update()
    time.sleep(inc) 
    print(inc)   
    rand_num = random.randrange(-300,301,20)
    color = random.choice(colors)
    obstacle = Obstacle((300,rand_num),color)
    hold.append(obstacle)
    for obstacle in hold:
        obstacle.move()
        
    if chick.ycor() > 300:
        chick.goto(0,-280)
        inc += 0.1
        # time.sleep(inc)
        level.add_score()
        print(inc)























screen.exitonclick()