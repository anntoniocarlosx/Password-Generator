
import random
import string
import tkinter as tk
import pyperclip


root = tk.Tk()

root.geometry("600x400")
root.title("Password Generator")
root.resizable(0, 0)

num = tk.IntVar()
length = tk.IntVar()
password = tk.StringVar()

# Number of passwords is 1 and length is 8 characters by default
num.set(1)
length.set(8)

# Length input thingy
tk.Label(root, text="LENGTH", font="arial 12").place(x=200, y=160)
tk.Entry(root, font="arial 12", textvariable=length, width=8).place(x=320, y=160)

# Another input thingy
tk.Label(root, text="NUMBER", font="arial 12").place(x=200, y=120)
tk.Entry(root, font="arial 12", textvariable=num, width=8).place(x=320, y=120)


def get_password():
    """Generate a random password"""

    chars = string.ascii_letters + string.digits + string.punctuation
    i = 0
    password_list = []

    if num.get() > 1:
        while i < num.get():
            new_password = "".join(random.sample(chars, length.get()))
            password_list.append(new_password)

            i += 1

        password_str = "   ".join(password_list) # The passwords are separated by 3 blank spaces
        password.set(password_str)

    elif num.get() == 1:
        new_password = "".join(random.sample(chars, length.get()))
        password.set(new_password)
    
    # I should handle the case where num is 0, maybe display a error message, but I'm not sure about how to do this


def save():
    """Save the password in a txt file""" # Not a really necessary feature, but I wanted to play around with some txt files

    try:
        with open("passwords.txt", "a") as password_file:
            print()
            # do something

    except FileNotFoundError:
        with open("passwords.txt", "x") as password_file:
            print()
            # do something


def copy_to_clipboard():
    """Copy the password to the clipboard."""
    pyperclip.copy(password.get())


def exit_window():
    """Exits the program"""
    root.destroy()

# Buttons
tk.Button(
    root,
    font="times 12 bold",
    text="GENERATE PASSWORD",
    width=20,
    command=get_password,
    bg="limegreen",
    padx=6,
).place(x=200, y=200)

tk.Button(
    root,
    font="times 12 bold",
    text="EXIT",
    width=10,
    command=exit_window,
    bg="orangered",
    padx=2,
).place(x=250, y=280)

tk.Button(
    root,
    font="times 12 bold",
    text="COPY",
    width=10,
    command=copy_to_clipboard,
    bg="lightgray",
    padx=2,
).place(x=250, y=240)

# Display the password on the screen
tk.Label(
    root, font="times 24 bold", textvariable=password
).pack() 

root.mainloop()
