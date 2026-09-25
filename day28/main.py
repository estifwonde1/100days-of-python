from tkinter import *
import time

PINK = "#FFC0CB"
RED = "#FF0000"
GREEN = "#008000"
YELLOW = "#FFFF00"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK = 20
testers=["00:01","00:02","00:03","00:04","00:05","00:06"]


window = Tk()
window.title("Pomodro techinique")
tomato = PhotoImage(file ="tomato.png")

canvas = Canvas(width=525,height=550 )
canvas.create_image(260,270,image=tomato)
timer_change=canvas.create_text(260,290,text="00:00",fill="white" ,font=(FONT_NAME,35,"bold"))
canvas.pack()

def change_text(n):
    # timer_change=canvas.create_text(260,290,text="00:00",fill="white" ,font=(FONT_NAME,35,"bold"))
    canvas.itemconfig(timer_change,text=n)
    

def count_down():
 
    for n in testers:       
        print(n)
        change_text(n)
        time.sleep(1)
        canvas.after(1000,count_down)



        
        
    




reset = Button(text= "Reset" )
start=Button(text="start",command=count_down)
canvas.create_window(200,500,window=start)
canvas.create_window(350,500,window=reset)

    
    














window.mainloop()
