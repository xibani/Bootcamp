
from tkinter import *


def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)


window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)
# window.config(padx=100, pady=200)

# label
my_label = Label(text="I am a Label", font=("Arial", 24, "italic"))
my_label.config(text="The new text")
my_label.grid(column=0, row=0)
my_label.config(padx=100, pady=100)

# Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="New button")
new_button.grid(column=2, row=0)

# Entry
input = Entry(width=10)
print(input.get())
input.grid(column=3, row=2)


# Pack / Place / Grid

window.mainloop()
