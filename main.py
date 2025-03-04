from turtle import Turtle, Screen
import pandas

states_data = pandas.read_csv('50_states.csv')

dicted_states = states_data.to_dict()
print(dicted_states['state'][0])
print(dicted_states['x'][0])
print(dicted_states['y'][0])


def on_map(x_cor, y_cor, state):
    turtle = Turtle()
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(x_cor,y_cor)
    turtle.write(arg=f'{state}')


tim = Turtle()
screen = Screen()
screen.title("U.S, States Game")
image = "blank_states_img.gif"
screen.addshape(image)
tim.shape(image)
screen.title('Name the States')
score = 0
correct_guesses = []
all_states = dicted_states['state']
game_is_on = True

while game_is_on:
    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state's Name").title()
    for state in dicted_states['state']:
        if answer_state == dicted_states['state'][state]:
            on_map(x_cor=dicted_states['x'][state],y_cor=dicted_states['y'][state],state=dicted_states['state'][state])
            correct_guesses.append(answer_state)
            score += 1

    if answer_state == "Exit":
        states_to_learn = []
        for state in all_states:
            if all_states[state] not in correct_guesses:
                states_to_learn.append(dicted_states['state'][state])
        new_data = pandas.DataFrame(states_to_learn)
        new_data.to_csv('states_to_learn')
        break
screen.exitonclick()
