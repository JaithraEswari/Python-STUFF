from turtle import Turtle, Screen, clearscreen, reset, resetscreen
import turtle
import random


turtle.colormode(255)

timmy = Turtle()
screen = Screen()

def forward():
    timmy.forward(10)

def backward():
    timmy.backward(10)

def counter_clockwise():
    timmy.left(5)

def clockwise():
    timmy.right(5)


screen.onkey(key='w', fun=forward)
screen.onkey(key='s', fun=backward)
screen.onkey(key='a', fun=counter_clockwise)
screen.onkey(key='d', fun=clockwise)
screen.onkey(key='c', fun=resetscreen)
screen.listen()
screen.exitonclick()