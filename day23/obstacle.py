from turtle import Turtle


class Obstacle(Turtle):
    def __init__(self,positions,color):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(1,2)
        self.goto(positions)
        self.color(color)
        
    def move(self):
        self.backward(10)
    