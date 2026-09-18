from turtle import Turtle

class Score(Turtle):
    def __init__(self,position):
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.penup()
        self.shapesize(1,1)
        self.goto(position)
        self.score = 0
        self.write(f"LEVEL : {self.score}",font=("ariel",20,"bold"))
    def add_score(self):
        self.clear()
        self.score +=1
        self.write(f"LEVEL : {self.score}",font=("ariel",20,"bold"))
        
