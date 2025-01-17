COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

from turtle import Turtle
import random

# Seleccionar aleatoriamente el color del coche
def select_color():
    return random.choice(COLORS)

# Generar aleatoriamente una posicion de coche
def random_position():
    min_lim = -300 + 80
    max_lim = 300 - 80
    return random.randint(min_lim, max_lim)


class CarManager:
    def __init__(self):
        self.cars = []
        self.create_car()

    def create_car(self):
        num_cars = random.randint(0, 3)
        for _ in range(num_cars):
            car = Turtle()
            car.shape("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.color(select_color())
            car.goto(300, random_position())
            self.cars.append(car)
            print("test")

    def move(self):
        for car in self.cars:
            car.goto(car.xcor() - MOVE_INCREMENT, car.ycor())

        for car in self.cars:
            if car.xcor() < -320:
                self.cars.remove(car)



