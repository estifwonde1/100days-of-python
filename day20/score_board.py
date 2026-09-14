import turtle as t

score = 0
class Score(t.Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.shapesize(1,1)
        self.setpos(0,270)
    
    
    def add_score(self):
        global score

        score += 1
        self.clear()
        self.write(score,font=("ariel",20,"bold"))

