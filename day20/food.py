import random
import turtle as t


class Food(t.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5,0.5)
        self.color("green")
        self.speed("fastest")
        self.refresh()
    def refresh(self):
        self.clear()
        x_int = random.randint(-280,280)
        y_int = random.randint(-280,280)
        self.goto(x_int,y_int)
      