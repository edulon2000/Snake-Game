from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.x = 0
        self.penup()
        self.goto(0,265)
        self.color("white")
        self.hideturtle()
        self.write(f"Score: {self.x}",True, align= "center", font=("Arial", 24, "normal"))
        
    def score_refresh (self):
        self.clear()
        self.goto(0,265)
        self.x +=1
        self.write(f"Score: {self.x}",True, align= "center", font=("Arial", 24, "normal"))
    
    def game_over(self):
        super().__init__()
        self.penup()
        self.goto(0,0)
        self.color("white")
        self.hideturtle()
        self.write("Game Over!",True, align= "center", font=("Arial", 24, "normal"))
        