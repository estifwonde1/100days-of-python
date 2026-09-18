from turtle import Turtle

class Chicken(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("blue")
        self.setheading(90)
        self.goto(position)
        
    def move_up(self):
        self.goto(self.xcor(),self.ycor()+20)

