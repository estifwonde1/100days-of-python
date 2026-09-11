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
    





























screen.exitonclick()