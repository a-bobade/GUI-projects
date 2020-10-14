from tkinter import *

count = -1
run = False


def variable(mark):
    def value():
        if run:
            global count
            # before starting
            if count == -1:
                show = "Starting"
            else:
                show = str(count)
            mark['text'] = show
            # count increment after
            # every 1 second
            mark.after(1000, value)
            count += 1

    value()


# While Running
def Start(mark):
    global run
    run = True
    variable(mark)
    start['state'] = 'disabled'
    stop['state'] = 'normal'
    reset['state'] = 'normal'


# While stopped
def Stop():
    global run
    start['state'] = 'normal'
    stop['state'] = 'disabled'
    reset['state'] = 'normal'
    run = False


# For Reset
def Reset(label):
    global count
    count = -1
    if not run:
        reset['state'] = 'disabled'
        mark['text'] = 'Welcome'
    else:
        mark['text'] = 'Start'


bobzy = Tk()
bobzy.title("StopWatch")
bobzy.config(bg="green")
bobzy.geometry("300x200")
bobzy.resizable(0, 0)
mark = Label(bobzy, text="Welcome", fg="black", font="Times 25 bold", bg="green")
mark.pack()
start = Button(bobzy, text='Start', width=25, command=lambda: Start(mark))
stop = Button(bobzy, text='Stop', width=25, state='disabled', command=Stop)
reset = Button(bobzy, text='Reset', width=25, state='disabled', command=lambda: Reset(mark))
start.pack()
stop.pack()
reset.pack()
bobzy.mainloop()
