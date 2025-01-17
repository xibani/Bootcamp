
from tkinter import *
from tkinter import messagebox
import random
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    password_entry.delete(0, END)
    password = ""

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 6))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 8))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)

    # Añadir la contraseña al clipboard
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    # Check all the fields are completed
    website = website_entry.get().lower()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Ooops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("./data/data.json", "r") as data_file:
                # Read old data
                data = json.load(data_file)

        except FileNotFoundError:
            with open("./data/data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)
            with open("./data/data.json", 'w') as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #
def search_password():
    website_key = website_entry.get().lower()
    try:
        with open("./data/data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError as file_no_found:
        messagebox.showinfo(title=f"{file_no_found}", message="There is no any password saved")
    else:
        try:
            info_email = data[website_key]["email"]
            info_password = data[website_key]["password"]
        except KeyError as key_error:
            if website_key != "":
                messagebox.showinfo(title=f"{key_error}", message=f"There is no {website_key.upper()} password")
        else:
            messagebox.showinfo(title=f"{website_key}", message=f"Email: {info_email}\nPassword: {info_password}")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=15, pady=15)

canvas = Canvas(height=200, width=200)
candado_img = PhotoImage(file="./pics/logo.png")
canvas.create_image(100, 100, image=candado_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)


# Entries
website_entry = Entry(width=33)
website_entry.grid(column=1, row=1)
website_entry.focus()
email_entry = Entry(width=52)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "anderg@gmail.com")
password_entry = Entry(width=33)
password_entry.grid(column=1, row=3)


# Buttons
generate_button = Button(text="Generate Password", width=14, command=generate_password)
generate_button.grid(column=2, row=3)
search_button = Button(text="Search", width=14, command=search_password)
search_button.grid(column=2, row=1)
add_button = Button(text="Add", width=44, command=save)
add_button.grid(column=1, row=4, columnspan=2)









window.mainloop()
