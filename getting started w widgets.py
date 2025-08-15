# import libraries
from tkinter import *
from datetime import date

# window creation
root = Tk()
root.title("getting started with widgets")
root.geometry("400x300")

# add widgets and label
lbl = Label(text="Hey!", fg="white", bg="#072F5F", height=1, width=300)

# add label for getting name as input from user
# use entry widget to create text box
namelbl = Label(text="Full Name", bg="#3895D3")
entryname = Entry()

# function to display a message
def display():
    name = entryname.get() # read user input
    global message 
    message = "Welcome to this application! \nToday's date is:"
    greet = "Hello", name

    textbox.insert(END, greet)
    textbox.insert(END, message)
    textbox.insert(END, date.today())

# add text widget
textbox = Text(height=3)

# create button
btn = Button(text="begin", command=display, height=1, bg="#1261A0", fg="white")

# organize all widgets
lbl.pack()
namelbl.pack()
entryname.pack()
btn.pack()
textbox.pack()
