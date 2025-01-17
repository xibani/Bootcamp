
from tkinter import *

def conversion():
    mile = int(miles_input.get())
    km = mile * 1.609
    km_result.config(text=str(km))


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)


# entrada
miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

# Label
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

km_result = Label(text="0")
km_result.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

# Boton
button = Button(text="Calculate", command=conversion)
button.grid(column=1, row=2)


window.mainloop()
