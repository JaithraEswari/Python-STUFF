import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
bg_image = turtle.shape(image)

data = pandas.read_csv("50_states.csv")

all_states = data.state.to_list()

guessed_states = []

score = 0


game_is_on = True
while game_is_on:
    answer_state = screen.textinput(title=f"{score}/50 Guess the State", prompt="What's another state's name").capitalize() #type: ignore
    print(answer_state)
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("missing_states.csv")
        break
    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        states = data[data.state == answer_state]
        t.goto(int(states.x), int(states.y)) #type: ignore
        guessed_states.append(answer_state)
        t.write(f"{guessed_states[score]}", font=('Arial', 8, 'normal'))
        score += 1
        if score == 50:
            game_is_on = False


