from turtle import Turtle

class Block(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(3,1)
        self.color("white")
        self.goto(position)
        # self.speed("fastest")
    def move_up(self):
        if self.ycor() < 263:
            self.goto(self.xcor(),self.ycor()+20)       

    def move_down(self):
        if self.ycor() > -263:
            self.goto(self.xcor(),self.ycor()-20)
        


