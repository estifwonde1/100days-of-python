import turtle as t

mini = t.Turtle()

def move():
    mini.forward(50)
screen = t.Screen()
screen.listen()
screen.onkey(key ="space",fun=move)
screen.exitonclick()
