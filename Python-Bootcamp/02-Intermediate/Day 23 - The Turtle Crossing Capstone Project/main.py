import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car = CarManager()


screen.listen()
screen.onkey(player.move_turtle, "Up")

game_is_on = True
count = 0
while game_is_on:
    time.sleep(scoreboard.car_speed)
    screen.update()

    car.move()

    # Detectar si ha llegado al borde superior
    if player.ycor() > 230:
        # Reset de tortuga
        player.turtle_reset()
        # Aumentar score
        scoreboard.point()

    # Detectar colisiones
    for c in car.cars:
        if player.distance(c) < 10 and c.xcor() == player.xcor():
            game_is_on = False
            scoreboard.game_over()


    if count % 7 == 0:
        car.create_car()
    count += 1

screen.exitonclick()