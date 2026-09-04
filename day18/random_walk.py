import random
from turtle import Screen, Turtle

from shapes import colors

mini = Turtle()

walks = [0,90,180,270,360]
num_walks = 500
for _ in range(num_walks):
    pick = random.randint(0,len(colors)-1)
    randomize = colors[pick]   
    swag = random.randint(0,len(walks)-1)
    forr = walks[swag]
    mini.pensize(7)
    mini.speed("fast")
    mini.right(forr)
    mini.forward(30)
    mini.color(randomize)
    
   
    
 





screen = Screen()
screen.exitonclick()
