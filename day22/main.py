from turtle import Screen
from block import Block
from score_board import Score , Boundry
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)
ball = Ball()
block1 = Block((-390,0))
block2= Block((390,0))
segment = Boundry()
score1 = Score((-100,270))
score2 = Score((100,270))

screen.listen()
screen.onkey(key ="Up",fun=block2.move_up)
screen.onkey(key ="Down",fun=block2.move_down)
screen.onkey(key= "w",fun=block1.move_up)
screen.onkey(key="s",fun=block1.move_down)


game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()  
    ball.move()

    if ball.ycor() > 290  or ball.ycor() < -290 :
        ball.bounce()
    if block2.distance(ball) < 15:
        print("thck")
        ball.bounce_back()
    if block1.distance(ball) < 15:
        print("thck")
        ball.bounce_back()
    if ball.xcor() > 395:
        score1.add_score()
        ball.refresh()
        ball.move()
        
    if ball.xcor() < -395:
        ball.refresh()
        score2.add_score()
       

   
      





screen.exitonclick()
