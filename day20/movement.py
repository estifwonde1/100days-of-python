import turtle as t


screen = t.Screen()
screen.setup(width = 600,height = 600)
screen.title("test subject")
screen.bgcolor("black")
screen.tracer(0)
segment_postions =[(0,0),(-20,0),(-40,0)]
segments = []
for _ in segment_postions:
    snakey = t.Turtle("square")
    snakey.color("white")
    snakey.penup()
    snakey.goto(_)
    segments.append(snakey)
is_game_on = True
while is_game_on:
    for seg_num in range(len(segments)-1,0,-1):
        new_x = segments(seg_num-1).xcor()
        new_y = segments(seg_num-1).ycor()
        seg_num.goto(new_x,new_y)

    snakey.forward(10)
    





























screen.exitonclick()