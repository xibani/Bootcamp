# from turtle import Turtle, Screen
# import random
#
# import heroes
# print(heroes.gen())
#
# tim = Turtle()
# #tim.shape("turtle")
# tim.color("blue violet")
#
#
# def make_square(length):
#     for _ in range(4):
#         tim.forward(length)
#         tim.right(90)
#
# def dashed_line(length, repeat=15):
#     for _ in range(repeat):
#         tim.forward(length)
#         tim.penup()
#         tim.forward(length)
#         tim.pendown()
#
# # Funcion para generar colores aleatorios
# def change_color():
#     R = random.random()
#     G = random.random()
#     B = random.random()
#
#     tim.color(R, G, B)
#
# # repetir una secuencia de moverse hacia adelante y girar x grados (la distancia fija)
# def forward_turn(angle):
#     tim.forward(100)
#     tim.right(angle)
#
# def make_shapes(n_shapes):
#     for i in range(3, n_shapes):
#         change_color()
#         angle = 360.0 / i
#         for _ in range(i):
#             forward_turn(angle)
#
#
# # Movimientos aleatorios
# def random_walks():
#     tim.pensize(5)
#     tim.speed("fastest")
#     for _ in range(2000):
#         change_color()
#         directions = [0, 90, 180, 270]
#         tim.forward(15)
#         tim.setheading(random.choice(directions))
#
#
# # Spirograph
# def spirograph(diameter, n_circles):
#     tim.speed("fastest")
#     angle = 360.0 / n_circles
#     for _ in range(n_circles):
#         change_color()
#         tim.circle(diameter)
#         tim.left(angle)
#
#
# spirograph(150, )


import random
import turtle as turtle_mode
from turtle import Screen

turtle_mode.colormode(255)
damian = turtle_mode.Turtle()
damian.speed("fastest")
damian.penup()
damian.hideturtle()
color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]

damian.setheading(225)
damian.forward(250)
damian.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    damian.dot(20, random.choice(color_list))
    damian.forward(50)

    if dot_count % 10 == 0:
        damian.setheading(90)
        damian.forward(50)
        damian.setheading(180)
        damian.forward(10 * 50)
        damian.setheading(0)








screen = Screen()
screen.exitonclick()

