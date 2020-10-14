# Emmanuel Abobade Simple Interest Calculator

# Import all functions/classes from tkinter
from tkinter import *


# Function to calculate the simple interest
def calculate():
    principal = float(principal_field.get())
    rate = float(rate_field.get())
    time = float(time_field.get())
    SI = (principal * rate * time) / 100
    simple_field.insert(0, SI)


# Function to clear all entries
def clear_all():
    principal_field.delete(0, END)
    rate_field.delete(0, END)
    time_field.delete(0, END)
    simple_field.delete(0, END)

    principal_field.focus_set()

# Create a GUI Window
bobzy = Tk()
bobzy.configure(background="sky blue")
bobzy.title("Simple Interest Calculator")
bobzy.geometry("320x300")
bobzy.resizable(0, 0)

# Creating Labels
label1 = Label(bobzy, text="Principal", bg="sky blue", fg="black", font="TimesNewRomans 12")
label2 = Label(bobzy, text="Rate", bg="sky blue", fg="black", font="TimesNewRomans 12")
label3 = Label(bobzy, text="Time", bg="sky blue", fg="black", font="TimesNewRomans 12")
label4 = Label(bobzy, text="Simple Interest =", bg="sky blue", fg="black", font="TimesNewRomans 12")

# Adding grids to the Labels created
label1.grid(row=0, column=0, sticky=W)
label2.grid(row=1, column=0, sticky=W)
label3.grid(row=2, column=0, sticky=W)
label4.grid(row=4, column=0, sticky=W)

# Creating Entry for the Labels
principal_field = Entry(bobzy)
rate_field = Entry(bobzy)
time_field = Entry(bobzy)
simple_field = Entry(bobzy)

# Adding grids to the Entries created
principal_field.grid(row=0, column=1, sticky=W, padx=5, pady=5)
rate_field.grid(row=1, column=1, sticky=W, padx=5, pady=5)
time_field.grid(row=2, column=1, sticky=W, padx=5, pady=5)
simple_field.grid(row=4, column=1, sticky=W, padx=5, pady=5)

# Creating Buttons
but = Button(bobzy, text="Calculate", command=calculate)
but2 = Button(bobzy, text="Clear", command=clear_all)

# Adding grids to the Buttons created
but.grid(row=3, column=1)
but2.grid(row=5, column=1)

# Start the GUI
bobzy.mainloop()