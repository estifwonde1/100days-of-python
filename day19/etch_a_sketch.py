import turtle as t

mini = t.Turtle()

def move_forward():
    mini.forward(50)
def move_backward():
    mini.backward(50)
def move_left():
    mini.left(90)
def move_right():
    mini.right(90)



screen = t.Screen()
screen.listen()
screen.onkey(key ="w",fun=move_forward)
screen.onkey(key="s",fun=move_backward)
screen.onkey(key="a",fun=move_left)
screen.onkey(key="d",fun=move_right)
screen.exitonclick()
