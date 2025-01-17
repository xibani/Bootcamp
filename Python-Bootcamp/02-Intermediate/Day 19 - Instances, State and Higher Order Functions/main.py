
# #   Etch-A-Sketch
#
# from turtle import Turtle, Screen
#
# tim = Turtle()
# screen = Screen()
#
# move = 3
# degree = 2
#
# def move_forwards():
#     tim.forward(move)
#
# def move_backwards():
#     tim.forward(-move)
#
# def turn_left():
#     # 1ª forma
#     tim.left(degree)
#
#     # 2ª Forma
#     #new_heading = tim.heading() + 10
#     #tim.setheading(new_heading)
#
# def turn_right():
#     tim.left(-degree)
#
# def reset_game():
#     tim.reset()
#     # tim.clear()
#     # tim.penup()
#     # tim.home()
#     # tim.pendown()
#
# screen.listen()
# screen.onkeypress(key='w', fun=move_forwards)
# screen.onkeypress(key='s', fun=move_backwards)
# screen.onkeypress(key='a', fun=turn_left)
# screen.onkeypress(key='d', fun=turn_right)
# screen.onkeypress(key='c', fun=reset_game)
#
#
# screen.exitonclick()


# Trutle race
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)

is_race_on = False

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_positions = [-100, -60, -20, 20, 60, 100]
all_turtles = []

y_pos = 0
for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[y_pos])
    all_turtles.append(new_turtle)
    y_pos += 1

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)






screen.exitonclick()
