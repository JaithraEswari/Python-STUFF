from turtle import Turtle, Screen
import turtle
import random
rgb_colors = [(235, 22, 231), (69, 229, 232), (236, 35, 108), (221, 232, 237), (146, 28, 66), (239, 75, 35),
              (230, 237, 232), (7, 148, 94), (220, 171, 45), (182, 159, 48), (44, 191, 232), (28, 126, 194)]

turtle.colormode(255)

timmy = Turtle()
timmy.speed('fastest')


def horizontal():
    for _ in range(10):
        timmy.color(random.choice(rgb_colors))
        timmy.begin_fill()
        timmy.circle(5)
        timmy.end_fill()
        timmy.penup()
        timmy.forward(20)
        timmy.pendown()

def position():
    timmy.penup()
    timmy.left(90)
    timmy.forward(20)
    timmy.left(90)
    timmy.forward(200)
    timmy.right(180)
    timmy.pendown()

for _ in range (10):
    horizontal()
    position()


screen = Screen()
screen.exitonclick()

