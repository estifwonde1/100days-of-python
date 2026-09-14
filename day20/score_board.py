import turtle as t

score = 0
class Score(t.Screen):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.shapesize(1,1)
        self.setpos(0,270)
    
        self.write(score,font = ("ariel",20,"bold"))

