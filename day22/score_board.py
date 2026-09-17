import turtle as t


class Score(t.Turtle):
    
    def __init__(self,position):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.shapesize(1,1)
        self.goto(position)
        self.score = 0
        self.write(self.score,font=("ariel",20,"bold"))

        
          
    def add_score(self):
      
        self.clear()
        self.score +=1        
        self.write(self.score,font=("ariel",20,"bold"))
    # def game_over(self):
    #   self.goto(0,0)  
class Boundry(t.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shape("square")
        self.shapesize(1,0.5)  
        self.color("white")   
        self.create_segment()
    
    def create_segment(self):
        for segment in range (-300,300,20):
            self.penup()
            self.goto(0,segment)
            self.pendown()
            self.goto(0,segment + 10)
            self.penup()
            self.speed("fastest")
