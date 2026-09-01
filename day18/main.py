from turtle import Turtle,Screen

mini = Turtle()
mini.shape("turtle")
mini.color("blue")
lili = Turtle()
lili.shape("turtle")
lili.color("green")
n = 5
# for i in range (0,n):
#     mini.right(90)
#     mini.forward(100)
for _ in range (50):
    
    lili.pendown()
    lili.forward(15)
    lili.penup()
    lili.forward(10)
    lili.pencolor("brown")
  









screen = Screen()
screen.exitonclick()