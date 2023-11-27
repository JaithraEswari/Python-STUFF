from turtle import Turtle, Screen, clearscreen, reset, resetscreen
import random

is_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will wint the race? Enter a color: ')
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_coords = [-100, -60, -20, 20, 60 , 100]
turtles = []

for number in range(0,6):
    turtle_user = Turtle(shape='turtle')
    turtle_user.color(colors[number])
    turtle_user.penup()
    turtle_user.goto(x=-230, y=y_coords[number])
    turtles.append(turtle_user)

if user_bet:
    is_on = True

while is_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print('You have won')
            else:
                print('You have lost')

        random_distance = random.randint(0,10)
        turtle.forward(random_distance)

screen.exitonclick()