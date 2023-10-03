from turtle import Turtle, Screen
import pandas

tim = Turtle()
tim.hideturtle()
tim.penup()

screen = Screen()
screen.title('US States Guess')
screen.setup(width=750, height=600)
screen.bgpic("blank_states_img.gif")

guessed_states = []
guessed_on = True
data = pandas.read_csv("50_states.csv")
state = data['state'].to_list()
# x_cor = data['x'].to_list()
# y_cor = data['y'].to_list()


def exit_fun(guessed_states, state):
    unguessed_states = [st for st in state if st not in guessed_states]
    # for st in state:
    #     if st not in guessed_states:
    #         unguessed_states.append(st)
    new_data = pandas.DataFrame(unguessed_states)
    new_data.to_csv("Unguessed_states")
    tim.color('red')
    for un_st in unguessed_states:
        st_data = data[data.state == un_st]
        tim.goto(int(st_data.x), int(st_data.y))
        tim.write(un_st)
    tim.pensize(10)
    tim.color('Spring Green')
    tim.goto(0, 280)
    tim.write("Thanks for Playing the game")


while len(guessed_states) < 50:
    answer = screen.textinput(title=f"{len(guessed_states)}/50 Guess the State", prompt="What's another state name?").title()
    if answer == "Exit":
        exit_fun(guessed_states, state)
        break
    elif answer in state:
        guessed_states.append(answer)
        # index = state.index(answer)
        # tim.goto(x_cor[index], y_cor[index])
        state_data = data[data.state == answer]
        tim.goto(int(state_data.x), int(state_data.y))
        tim.write(answer)

screen.exitonclick()
