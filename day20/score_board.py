import turtle as t

class Score(t.Turtle):
    
    def __init__(self,position):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.score = 0
        self.high_score = 0
        self.speed("fastest")
        self.shapesize(1,1)       
        self.goto(position)
    
    
    def add_score(self):
        self.score += 1
        self.update_score()

    # def game_over(self):
    #   self.goto(0,0)         
    #   self.write("GAME OVER" ,align = "center" , font=("ariel",20,"bold"))
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score {self.high_score}",font=("ariel",20,"bold"))
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_score()


