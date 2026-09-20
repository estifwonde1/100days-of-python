import turtle as t
import pandas as pd

data=pd.read_csv("50_states.csv")

screen= t.Screen()
screen.setup(750,500)
screen.title("U.S states Game")
screen.register_shape("blank_states_img.gif")

maps=t.Turtle()
maps.shape("blank_states_img.gif")

state_name = data["state"].to_list()
guessed_names =[]
game_is_on = True
n = 0
while len(guessed_names) <50:

  
    answer_state = screen.textinput(title=f"{n}/50 Correct",prompt="what is another state")
    print(n)
    if answer_state == "Exit":
        missed_states=[state for state in state_name if state not in guessed_names]
        new_data = pd.DataFrame(missed_states)
        new_data.to_csv("states_to_learn.csv")
        break

    # missed_states=[state for state in state_name if state not in guessed_names]




    if answer_state in state_name:
        guessed_names.append(answer_state)
        answer = data[data.state == answer_state] 
        x_cor=answer.x.to_list()
        y_cor=answer.y.to_list()  
        n += 1
        put = t.Turtle()
        put.hideturtle()
        put.color("black")
        put.penup()
        put.goto(x_cor[0],y_cor[0])
        put.write(answer_state)
    else:
        answer_state = screen.textinput(title=f"{n}/50 Correct",prompt="what is another state")
    

















screen.exitonclick()