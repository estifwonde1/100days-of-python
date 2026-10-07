from tkinter import *
import random
import pandas as pd 
FONT_NAME = "Courier"

with open("/data/commom_french_words.csv") as file:
    data = file.read()
window = Tk()
window.title("Flash Card")
front_card = PhotoImage(file="images/frontpage.png")
back_card = PhotoImage(file="images/backpage.png")
right=PhotoImage(file="images/right.png")
wrong=PhotoImage(file="images/wrong.png")
canvas = Canvas(width=700,height=400)
switch = canvas.create_image(350,200,image=front_card)
canvas.grid(row=0,column=1)
timer_change = canvas.create_text(600,350, text ="00:00" ,fill="black",font=(FONT_NAME,35,"bold"))
# timer.grid(row = 0, column=2)

def click_right():
    count_down(5)
def click_wrong():
    count_down(5)

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
wrong_button = Button(image = wrong,command=click_wrong,bd=0)
wrong_button.grid(row=5,column=2)
















window.mainloop()