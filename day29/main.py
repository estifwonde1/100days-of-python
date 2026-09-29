from tkinter import *
import random 

window = Tk()
window.title("password generator")
lock = PhotoImage(file = "locks-removebg-preview.png")
canvas = Canvas(width = 350 ,height = 300)
canvas.create_image(200,150, image= lock)
canvas.grid(row= 0,column = 0 ,columnspan= 2,pady = 20)
website_label = Label(text = "Webiste:")
website_label.grid(row = 1,column = 0 ,padx=10,pady=10)
website_entry = Entry(width=30)
website_entry.grid(row = 1,column= 1,padx=10,pady=10)
email_label = Label(text = "Email/Username :")
email_label.grid(row=2,column =0,padx=10,pady=10)
email_entry=Entry(width = 30)
email_entry.grid(row=2,column=1,padx=10,pady=10)
password_label = Label(text = "Password :")
password_label.grid(row = 3,column = 0,padx=(5,5),pady=10)
password_entry = Entry(width =15)
password_entry.grid(row=3,column=1,padx=(5,2),pady=10)
generate_btn = Button(text = "Generate")
generate_btn.grid(row=3,column=2,padx=(1,10),pady=10)
add_btn = Button(text = "add",width=30)
add_btn.grid(row=4,column=1)










window.mainloop()
