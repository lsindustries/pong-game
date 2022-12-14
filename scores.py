from turtle import Turtle

class Scores(Turtle):

    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(position)
        self.scores_update()

    def scores_update(self):
        self.write(f"SCORE: {self.score}", align="center", font=("Arial", 12, "normal"))

    def get_point(self):
        self.score += 1
        self.clear()
        self.scores_update()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=("Arial", 30, "normal"))

