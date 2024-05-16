from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("snake_game\data_int.txt") as data:
            self.high_score = int(data.read())
        self.penup()
        self.goto(0,265)
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.goto(0,265)
        self.write(f"Score: {self.score} High Score:{self.high_score}",True, align= "center", font=("Courier", 24, "normal"))
        
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
        
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("snake_game\data_int.txt", mode="w") as data:
                data.write(f"{self.high_score}")         
        self.score=0
        self.update_scoreboard()
        