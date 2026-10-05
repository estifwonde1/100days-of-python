from tkinter import *



window = Tk()
window.title("Flash Card")
front_card = PhotoImage(file="images/frontpage.png")
back_card = PhotoImage(file="images/backpage.png")
right=PhotoImage(file="images/right.png")
wrong=PhotoImage(file="images/wrong.png")


canvas = Canvas(width=700,height=400)
canvas.create_image(350,200,image=front_card)
canvas.grid(row=0,column=0)
canvas.create_image(200,200,image=right)
canvas.grid(row=5,column=0)

















window.mainloop()