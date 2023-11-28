import time
from turtle import Screen
from player import STARTING_POSITION, Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

timmy = Player()
score = Scoreboard()
cars = CarManager()

screen.listen()
screen.onkeypress(timmy.up, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.movement()

    if timmy.ycor() > 280:
        score.next_level()
        timmy.goto(STARTING_POSITION)
        cars.increase_speed()

    for i in cars.all_car:
        if timmy.distance(i) < 20:
            game_is_on = False
            score.gameover()


screen.exitonclick()
