from turtle import Screen
from block import Block
from score_board import Score , Boundry

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")

block1 = Block()
block1.goto(-390,0)
block2= Block()
block2.goto(390,0)
segment = Boundry()
score1 = Score((-100,270))
score2 = Score((100,270))

screen.listen()
screen.onkey(key ="Up",fun=block2.move_up)
screen.onkey(key ="Down",fun=block2.move_down)
screen.onkey(key= "w",fun=block1.move_up)
screen.onkey(key="s",fun=block1.move_down)








screen.exitonclick()
