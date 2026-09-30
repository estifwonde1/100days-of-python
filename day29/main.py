import random
import string
from tkinter import *
from tkinter import messagebox
import pyperclip
import json


rand_num = random.randint(1, 100)
letters = list(string.ascii_letters)
numbers = list(string.digits)
special_char = list(string.punctuation)
password = []
window = Tk()
window.title("password generator")
lock = PhotoImage(file="locks-removebg-preview.png")
canvas = Canvas(width=350, height=300)
canvas.create_image(200, 150, image=lock)
canvas.grid(row=0, column=0, columnspan=2, pady=20)
website_label = Label(text="Webiste:")
website_label.grid(row=1, column=0, padx=10, pady=10)
website_entry = Entry(width=15)
website_entry.focus()
website_entry.grid(row=1, column=1, padx=10, pady=10)
email_label = Label(text="Email/Username :")
email_label.grid(row=2, column=0, padx=10, pady=10)
email_entry = Entry(width=30)
email_entry.insert(0, "estifwonde211@gmail.com")
email_entry.grid(row=2, column=1, padx=10, pady=10)
password_label = Label(text="Password :")
password_label.grid(row=3, column=0, padx=(5, 5), pady=10)
password_entry = Entry(width=15)
password_entry.grid(row=3, column=1, padx=(5, 2), pady=10)


def generator():
    for _ in range(9):
        password.append(random.choice(letters))
        password.append(random.choice(numbers))
        password.append(random.choice(special_char))
    random.shuffle(password)
    final_password = "".join(password)
    password_entry.insert(0, final_password)


def add():
    website = website_entry.get()
    user_name = email_entry.get()
    password = password_entry.get()
    new_data = {website: {"username": user_name, "password": password}}
    if len(website) < 1 or len(password) < 1:
        messagebox.showerror("invalid inputs", "inputs can't be empty")
    else:
        answer = messagebox.askyesno(
            "Comfirmation",
            f"Are u sure u want to save the password : {password} for this website: {website}",
        )
        if answer:
            try:
                with open("data.json", "r") as file:
                    data = json.load(file)
            except FileNotFoundError:
                with open("data.json", "w") as file:
                    json.dump(new_data, file, indent=4)
                    website_entry.delete(0, END)
                    password_entry.delete(0, END)
                    print(f"\n{website}|{user_name}|{password}")
                pyperclip.copy(password)

            else:
                data.update(new_data)
                with open("data.json", "w") as file:
                    json.dump(data, file, indent=4)
                    pyperclip.copy(password)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                print(f"\n{website}|{user_name}|{password}")

        else:
            return


def Search():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo("file not found", "the email has not been saved")
    else:
        if website in data:
            messagebox.showinfo(
                "File found",
                f"here is the Username:{data[website]['username']}\nPassword:{data[website]['password']}",
            )
            pyperclip.copy(data[website]["password"])
        else:
            messagebox.showerror("file not found", "the website has not been saved")
    finally:
        website_entry.delete(0, END)


generate_btn = Button(text="Generate", command=generator)
generate_btn.grid(row=3, column=2, columnspan=2, padx=(1, 10), pady=10)
add_btn = Button(text="add", width=30, command=add)
add_btn.grid(row=4, column=1)
search_btn = Button(text="Search", command=Search)
search_btn.grid(row=1, column=2, columnspan=2, padx=(1, 10), pady=10)


window.mainloop()
