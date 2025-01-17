FONT = ("Courier", 24, "normal")

from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.car_speed = 0.1
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-240, 260)
        self.write(f"Level: {self.score}", align="center", font=("Courier", 18, "bold"))

    def point(self):
        self.score += 1
        self.car_speed *= 0.9
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align='center', font=('Arial', 22, 'normal'))

