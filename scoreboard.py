from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-100, 200)
        self.write(self.left_score, align="center", font=("Arial", 50, "normal"))
        self.goto(100, 200)
        self.write(self.right_score, align="center", font=("Arial", 50, "normal"))

    def increase_left_score(self):
        self.left_score += 1
        self.clear()
        self.update_scoreboard()

    def increase_right_score(self):
        self.right_score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self, player):
        self.goto(0, 0)
        self.write(f"Game Over. {player} won the game.", align="center", font=("Arial", 25, "normal"))

