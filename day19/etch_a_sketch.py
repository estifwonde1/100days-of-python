import turtle as t

mini = t.Turtle()

def move_forward():
    mini.forward(10)
def move_backward():
    mini.backward(10)
def move_left():
    new_heading = mini.heading() + 10
    mini.setheading(new_heading)
   
def move_right():
    new_heading = mini.heading() - 10
    mini.setheading(new_heading)

def clear():
    
    mini.setpos(0,0)
    mini.setheading(0)
    mini.clear()



screen = t.Screen()
screen.listen()
screen.onkey(key ="w",fun=move_forward)
screen.onkey(key="s",fun=move_backward)
screen.onkey(key="a",fun=move_left)
screen.onkey(key="d",fun=move_right)
screen.onkey(key="c",fun=clear)

screen.exitonclick()
