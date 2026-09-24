from tkinter import *

window = Tk()
window.title("Mile to Km converter")
window.minsize(width=300,height=200)

miles_entry = Entry(width=10)
miles_entry.grid(column=1,row=4)
miles_label=Label(text = "Miles")
miles_label.grid(column=1,row=5)

Km_label = Label(text = " ")
Km_label.grid(column = 2 , row = 4)
text = Label(text="is equal to ")
text.grid(column = 1,row = 5)
Km = Label(text = "KM")
Km.grid(column=2,row = 5)

def convert():
    miles =miles_entry.get()
    Km = float(miles) * 1.609344
    Km_label.config(text = Km)

conver = Button(text = "convert", command =convert)
conver.grid(column= 1,row=6)
    





# my_label = Label(text="label", font=("Ariel",24,"bold"))
# my_label.grid(column=0,row=0)

# # button
# # my_label = Label(text="I got clicked", font=("Ariel",24,"bold"))
# # my_label.pack(expand=True)


# #entry
# def Update():
#     user_input=my_entry.get()
#     my_label.config(text=user_input)
#     my_label.grid(column=0,row=0)
    
# my_entry = Entry()
# my_entry.grid(column=3,row=2)
# # def button_click():
# #     my_label = Label(text="I got clicked", font=("Ariel",24,"bold"))
# #     my_label.pack(expand=True)
# #     print("i got clicked")
# my_button = Button(text ="CLick me",command=Update)
# my_button.grid(column=3,row=4)
# second_button=Button(text = "New Button")
# second_button.grid(column=4,row=0)








window.mainloop()