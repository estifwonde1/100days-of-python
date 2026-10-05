from tkinter import *
import math


FONT_NAME = "Courier"
window = Tk()
window.title("Flash Card")
front_card = PhotoImage(file="images/frontpage.png")
back_card = PhotoImage(file="images/backpage.png")
right=PhotoImage(file="images/right.png")
wrong=PhotoImage(file="images/wrong.png")
canvas = Canvas(width=700,height=400)
canvas.create_image(350,200,image=front_card)
canvas.grid(row=0,column=1)
timer_change = canvas.create_text(350,200, text ="00:00" ,fill="black",font=(FONT_NAME,35,"bold"))
# timer.grid(row = 0, column=2)

def click():
    print("button clicked")

def count_down(count):
    count_sec =  count %60
    if count_sec > -1:
        canvas.itemconfig(timer_change,text =f"{count_sec}")
        window.after(1000,count_down,count-1)
        print("worked")
    else:
        count_down(30)
count_down(30)


right_button = Button(image = right,command=click,bd=0)
right_button.grid(row=5,column=0)
wrong_button = Button(image = wrong)
wrong_button.grid(row=5,column=2)
















window.mainloop()