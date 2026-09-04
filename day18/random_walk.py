import random
from turtle import Screen, Turtle

from shapes import colors

mini = Turtle()

walks = [0,90,180,270]

for _ in range(200):
    pick = random.randint(0,len(colors)-1)
    randomize = colors[pick]   
    mini.pensize(7)
    mini.speed("fast")
    mini.setheading(random.choice(walks))
    mini.forward(30)
    mini.color(randomize)
    
   
    
 





screen = Screen()
screen.exitonclick()
