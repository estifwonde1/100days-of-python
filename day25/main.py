import turtle as t
import pandas as pd

data=pd.read_csv("50_states.csv")

screen= t.Screen()
screen.setup(750,500)
screen.title("U.S states Game")
screen.register_shape("blank_states_img.gif")

maps=t.Turtle()
maps.shape("blank_states_img.gif")
state_xcor =data["x"].to_list()
state_ycor = data["y"].to_list()
state_name = data["state"].to_list()
game_is_on = True
n = 0
while game_is_on:
  
    answer_state = screen.textinput(title=f"{n}/50 Correct",prompt="what is another state")
    print(n)

    if answer_state in state_name:
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