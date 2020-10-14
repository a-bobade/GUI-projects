# Import all functions/classes from tkinter
import time
from tkinter import *

# Create a GUI Window
bobzy = Tk()
bobzy.title("Digital Clock")
bobzy.geometry("350x200")
bobzy.resizable(0, 0)

# Adding a label
label = Label(bobzy, font=("Courier", 30, 'bold'), bg="black", fg="white", bd=80)
label.grid(row=0, column=1)


# Creating a function for the current time
def digitalclock():
    text_input = time.strftime("%H:%M:%S")
    label.config(text=text_input)
    label.after(200, digitalclock)


digitalclock()

# Start the GUI
bobzy.mainloop()
