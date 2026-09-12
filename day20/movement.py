import turtle as t
import time


screen = t.Screen()
screen.setup(width = 600,height = 600)
screen.title("test subject")
screen.bgcolor("black")
screen.tracer(0)
segment_postions =[(0,0),(-20,0),(-40,0)]
segments = []
for postions in segment_postions:
    snakey = t.Turtle(shape = "square")
    snakey.color("white")
    snakey.penup()
    snakey.goto(postions)
    segments.append(snakey)
is_game_on = True
while is_game_on:
    for seg_num in range(len(segments)-1,0,-1):
        new_x = int(segments[seg_num-1].xcor())
        new_y = int(segments[seg_num-1].ycor())
        print(new_x,new_y)
        segments[seg_num].goto(new_x,new_y)

    time.sleep(0.3)
    snakey.forward(10)
    snakey.right(90)
    snakey.forward(10)
    
    screen.update()
    





























screen.exitonclick()