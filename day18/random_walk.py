import random
import turtle as t

mini = t.Turtle()
t.colormode(255)
def colors():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

walks = [0,90,180,270]

for _ in range(200):   
    mini.pensize(7)
    mini.speed("fast")
    mini.setheading(random.choice(walks))
    mini.forward(30)
    mini.color(colors())
    
   
    
 





screen = t.Screen()
screen.exitonclick()
