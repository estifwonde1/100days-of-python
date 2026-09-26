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
testers=["00:00","00:01","00:02","00:03","00:04","00:05","00:06"]


window = Tk()
window.title("Pomodro techinique")
tomato = PhotoImage(file ="tomato.png")
canvas = Canvas(width=525,height=550 )
canvas.create_image(260,270,image=tomato)
timer_change=canvas.create_text(260,290,text= 0 ,fill="white" ,font=(FONT_NAME,35,"bold"))
canvas.pack()

# def say_something(a,b,c,):
    

#     print(a)
#     print(b)
#     print(c)
def counter(count):
    count_min = math.floor(count/60)
    count_sec =count%60
    if count_sec == 0:
        count_sec = "00"
    print(count)
    if count > -1:
        canvas.itemconfig(timer_change, text = f"{count_min}:{count_sec}")
        window.after(1000,counter,count - 1)

    



def accept():        
    counter(5 * 60)




reset = Button(text= "Reset" )
start=Button(text="start",command=accept)
canvas.create_window(200,500,window=start)
canvas.create_window(350,500,window=reset)

    
    














window.mainloop()
