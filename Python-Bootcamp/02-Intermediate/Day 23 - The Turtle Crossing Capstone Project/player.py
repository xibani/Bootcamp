STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)

    def move_turtle(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def turtle_reset(self):
        self.goto(STARTING_POSITION)


