from tkinter import *
import math

PINK = "#FFC0CB"
RED = "#FF0000"
GREEN = "#008000"
YELLOW = "#FFFF00"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK = 20
rep = 0
testers=["00:00","00:01","00:02","00:03","00:04","00:05","00:06"]


window = Tk()
window.title("Pomodro techinique")
tomato = PhotoImage(file ="tomato.png")
canvas = Canvas(width=525,height=550 )
canvas.create_image(260,270,image=tomato)
timer_change=canvas.create_text(260,290,text= "00:00" ,fill="white" ,font=(FONT_NAME,35,"bold"))
title_lable = canvas.create_text(260,400,text = "WORK",fill="green",font=(FONT_NAME,45,"bold"))

canvas.pack()

def count_down(count): 
    count_min = math.floor(count/60)
    count_sec =count%60
    if count_sec < 10:
        count_sec = f"0{count_sec}" 
    if count > -1:
        canvas.itemconfig(timer_change, text = f"{count_min}:{count_sec}")
        window.after(1000,count_down,count - 1)
    else:
        start_timer() 

def start_timer():
    global rep 
    rep +=1
    work_min = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK * 60
    if rep % 8 == 0:
        count_down(long_break)
        canvas.itemconfig(title_lable, text = "LONG BREAK",fill="black")
    elif rep % 2 ==0:
        count_down(short_break)
        canvas.itemconfig(title_lable, text="SHORT BREAK",fill="pink")
    else:
        count_down(work_min)
 

reset = Button(text= "Reset" )
start=Button(text="start",command=start_timer)
canvas.create_window(200,500,window=start)
canvas.create_window(350,500,window=reset)

    
    














window.mainloop()
