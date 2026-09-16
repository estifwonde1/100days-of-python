from turtle import Turtle

class Block(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(3,1)
        self.color("white")
        # self.speed("fastest")
    def move_up(self):
        self.goto(self.xcor(),self.ycor()+20)       

    def move_down(self):
        self.goto(self.xcor(),self.ycor()-20)
        


