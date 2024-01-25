import tkinter as tk
from tk import *
from tkinter import ttk, messagebox

def button_func():
    print('a button was pressed')

# commands run when window closed
def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()

# placeholder function for anything that requires a function that hasn't been written yet
def void():
    return None

#import sv_ttk

# create window
root = tk.Tk()
root.title('Window and Widgets')
root.geometry('800x500')

# menubar
menubar = tk.Menu(master=root)
filemenu = tk.Menu(master=menubar, tearoff=0)
filemenu.add_command(label="New", command=void)
filemenu.add_command(label="Open", command=void)
filemenu.add_command(label="Save", command=void)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

# ttk label
label = ttk.Label(master=root, text="this is a test")
label.pack()

# tk.Text
text = tk.Text(master=root)
text.pack()

# ttk.Entry
entry = ttk.Entry(master=root)
entry.pack()

# function button
button = ttk.Button(master=root, text='button', command=button_func)
button.pack()

#sv_ttk.set_theme("dark")

root.config(menu=menubar)
root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()