import turtle as t

class Food():
    def __init__(self):
        self.food = t.Turtle("circle")
        self.food.color("green")
        self.food.shapesize(0.5,0.5)
        self.food.penup()
    def appear(self,x_pos,y_pos):
        self.food.goto(x_pos,y_pos)