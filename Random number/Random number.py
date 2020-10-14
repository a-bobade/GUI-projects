from tkinter import *
import random


def generate():
    lower = int(lower_limit.get())
    upper = int(upper_limit.get())
    random_no = random.randint(lower, upper)
    generated.insert(0, random_no)


def clear():
    lower_limit.delete(0, END)
    upper_limit.delete(0, END)
    generated.delete(0, END)

    lower_limit.focus_set()


bobzy = Tk()
bobzy.title("Random Number Generator")
bobzy.geometry("320x250")
bobzy.configure(background="sky blue")
bobzy.resizable(0, 0)

label1 = Label(bobzy, text="Random Number Generator", fg="dark blue", bg="sky blue",
               font=("TimesNewRomans", 15, "bold"))
label2 = Label(bobzy, text="This version of the generator creates a random integer"
                           "\nup to a few thousand digits.", bg="sky blue")
label3 = Label(bobzy, text="Lower Limit", bg="sky blue", font=("TimesNewRomans", 10, "bold"))
label4 = Label(bobzy, text="Upper Limit", bg="sky blue", font=("TimesNewRomans", 10, "bold"))
label5 = Label(bobzy, text="Number =", bg="sky blue", font=("TimesNewRomans", 11, "bold"))

label1.grid(row=0, column=0, padx=7, pady=7, sticky=W)
label2.grid(row=1, column=0, padx=7, pady=7, sticky=W)
label3.grid(row=2, column=0, sticky=W)
label4.grid(row=3, column=0, sticky=W)
label5.grid(row=6, column=0, sticky=W)

lower_limit = Spinbox(bobzy, from_=1, to=100, width=20)
upper_limit = Spinbox(bobzy, from_=1, to=100, width=20)
generated = Entry(bobzy, width=22)

lower_limit.grid(row=2, rowspan=1)
upper_limit.grid(row=3, rowspan=1)
generated.grid(row=6, rowspan=1)

but1 = Button(bobzy, text="Generate", bg="green", command=generate)
but2 = Button(bobzy, text="Clear", bg="grey", command=clear)

but1.grid(row=4, column=0, rowspan=1)
but2.grid(row=5, column=0, rowspan=1)

bobzy.mainloop()
