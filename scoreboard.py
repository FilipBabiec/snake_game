from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        with open("highscore.txt", mode="r") as f:
            self.highscore = int(f.read())
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}    High score: {self.highscore}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
        with open("highscore.txt", mode="w") as f:
            f.write(str(self.highscore))
        self.score = 0

    def increase_score(self):
        self.score += 1
        if self.score > self.highscore:
            self.highscore = self.score
        self.clear()
        self.update_scoreboard()
