import turtle as t
import random


screen = t.Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("snakey cake")
score_board = t.Turtle()
score_board.hideturtle()
score = 0
score_board.color("white")

score_board.penup()
score_board.speed("fastest")
score_board.shapesize(1,1)
score_board.setpos(0,280)
score_board.write(score,font =("ariel",20,"bold"))


segement_postions = [(0,0),(-20,0),(-40,0)]
fully = []
for _ in segement_postions:
    snakey = t.Turtle(shape = "square")
    snakey.color("white")
    snakey.penup()
    snakey.goto(_)
    fully.append(snakey)
is_gameover = True
#food section myboy don't forget
food = t.Turtle("circle")
food.color("green")
food.shapesize(0.5,0.5)
food.penup()
x_pos = random.randint(-300,300)
y_pos = random.randint(-300,300)
food.speed("fastest")
food.setpos(x_pos,y_pos)
while is_gameover:   
    snakey.penup()
    snakey.forward(10)
    snakey.speed(1)
    for snake in fully:
        if snake.xcor() > 280 or snake.xcor() < -280 or snake.ycor() > 280 or snake.ycor() < -280:
            is_gameover = False
        def move_right():
            new_heading = snakey.heading() + 90
            snakey.setheading(new_heading)
        def move_left():
            new_heading = snakey.heading() - 90
            snakey.setheading(new_heading)
        if snake.distance(food)<15:
            x_pos = random.randint(-300,300)
            y_pos = random.randint(-300,300)
            food.clear()
            food.goto(x_pos,y_pos)
            score_board.clear()          
            score += 1
            score_board.write(score,font =("ariel",20,"bold"))
            # score_board.write(score)
            print(snake.position(),food.position())




    screen.listen()
    screen.onkey(key ="d",fun = move_right)
    screen.onkey(key = "a",fun = move_left)
    














screen.exitonclick()