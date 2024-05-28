from turtle import Turtle

ALIGN = "center"
FONT = ("courier", 24, "normal")


class Score_board(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.penup()
        self.goto(0, 250)
        self.color("white")
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"score:{self.score} Highscore:{self.highscore}", align=ALIGN, font=FONT)

    def reset_score(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt","w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()
