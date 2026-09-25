from tkinter import *
from PIL import ImageTk,Image
import time

PINK = "#FFC0CB"
RED = "#FF0000"
GREEN = "#008000"
YELLOW = "#FFFF00"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK = 20


window = Tk()
window.title("Pomodro techinique")
tomato = Image.open("Tomato.jpg")
tk_image = ImageTk.PhotoImage(tomato)

image_label =Label(image = tk_image)
def count_down(down):
 
    for n in range(0,down):
        time.sleep(1)
        print(n)
    
count =Label(text=30)
count.grid(column = 1, row = 1)


count_down(10)

    
    














window.mainloop()
