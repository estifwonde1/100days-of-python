import random
import turtle as t

mini = t.Turtle()
t.colormode(255)
def colors():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return(r,g,b)

def circles():
    n = 360
    m = 0
    while m <= n:
        
        # heads = 360 / n
        mini.speed("fastest")
        mini.circle(100)
        mini.setheading(m)
        mini.color(colors())   
        m += 5
        


circles()


















screen = t.Screen()
screen.exitonclick()