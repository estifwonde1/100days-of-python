from tkinter import *
import random
import pandas as pd 
import json

FONT_NAME = ("arial",25,"italic")
BACKGROUND_COLOR = "#B1DDC6"
with open("data/common_french_words.csv") as file:
    data = file.read()
data = pd.read_csv("data/common_french_words.csv")
to_learn = data.to_dict(orient="records")
print(to_learn)
window = Tk()
window.title("Flash Card")
front_card = PhotoImage(file="images/frontpage.png")
back_card = PhotoImage(file="images/backpage.png")
right=PhotoImage(file="images/right.png")
wrong=PhotoImage(file="images/wrong.png")
canvas = Canvas(width=700,height=400)
switch = canvas.create_image(350,200,image=front_card)
canvas.create_text(350,30, text= "Title",font = FONT_NAME )
card_name = canvas.create_text(350,200, text= "Card", font= FONT_NAME)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness= 0)
canvas.grid(row=0,column=1)
timer_change = canvas.create_text(600,350, text ="00:00" ,fill="black",font=(FONT_NAME,35,"bold"))
# timer.grid(row = 0, column=2)

def click_right():
    current = random.choice(to_learn(0))
    canvas.itemconfig(card_name, text =f"{current}")
#     count_down(5)
# def click_wrong():
#     count_down(5)

def count_down(count):
    count_sec =  count %60
    if count_sec == 0:
        canvas.itemconfig(switch,image=back_card)
    else:
        canvas.itemconfig(switch,image=front_card)
    if count_sec > 0:
        canvas.itemconfig(timer_change,text =f"{count_sec}")
        window.after(1000,count_down,count-1)
        print("worked")
   
count_down(5)


right_button = Button(image = right,command=click_right,bd=0)
right_button.grid(row=5,column=0)
wrong_button = Button(image = wrong,command=click_right,bd=0)
wrong_button.grid(row=5,column=2)
















window.mainloop()