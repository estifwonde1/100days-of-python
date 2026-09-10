import turtle as t


screen = t.Screen()
screen.setup(width = 600,height = 600)
screen.title("test subject")
screen.bgcolor("black")
screen.tracer(0)
head = t.Turtle(shape = "square")
head.penup()
lead = head.pos()
head.color("white")

segment_postions =[(-20,0),(-40,0)]
bodies = []
for _ in segment_postions:
    mini = t.Turtle(shape="square")
    mini.color("white")
    mini.penup()
    bodies.append(mini)
moving = True
pos_history = []
step_delay = 3
def move():
    pos_history.insert(0,head.pos())
    head.forward(10)
    head.speed(1)
    for index , mini in enumerate(bodies):
        history = (index + 1) * 3
        if len(pos_history) > history:
            mini.goto(pos_history[history])
    if len(pos_history) > 10:
        pos_history.pop()
    screen.update()
    screen.ontimer(move,20)


def move_right():
    new_heading = head.heading() + 90
    head.setheading(new_heading)
def move_left():
    new_heading = head.heading() - 90
    head.setheading(new_heading)
screen.listen()
screen.onkey(key="d",fun = move_right)
screen.onkey(key="a",fun = move_left)
move()
# while moving:
#     for body in bodies:
#         head.forward(10)
#         head.speed(0)
#         body.forward(10)
#         body.speed(1)
        
#     if body.xcor() > 280:
#         moving = False
#     def move_right():
#         for body in bodies:
#             new_heading = head.heading() + 90
#             head.setheading(new_heading )
#             body.setheading(new_heading)
#     screen.listen()
#     screen.onkey(key = "d" ,fun =move_right)


    

































screen.exitonclick()