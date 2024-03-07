import pandas
import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")

states_list = data["state"].to_list()
states_gotten_correct = []
# print(states_list)


while len(states_gotten_correct) < 50:
    answer_state = screen.textinput(title=f"{len(states_gotten_correct)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = [state for state in states_list if state not in states_gotten_correct]
        states_to_learn = {"States to learn": missing_states}
        df = pandas.DataFrame(states_to_learn)
        df.to_csv("states_to_lean.csv")
        break
    if answer_state in states_list and answer_state not in states_gotten_correct:
        state_data = data[data["state"] == answer_state]
        state_name = state_data["state"].iloc[0].title()
        state_x = state_data["x"].iloc[0]
        state_y = state_data["y"].iloc[0]

        states_gotten_correct.append(state_name)

        writer = turtle.Turtle()

        writer.penup()
        writer.hideturtle()
        writer.goto(state_x, state_y)
        writer.write(f"{state_name}", align="center", font=("Courier", 10, "normal"))
