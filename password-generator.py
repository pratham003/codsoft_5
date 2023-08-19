import random
import pyperclip
import tkinter as tk
from tkinter import IntVar
from tkinter.ttk import *


def generate_password():
    length = length_var.get()
    strength = strength_var.get()
    characters = ""

    if strength == 1:
        characters = "abcdefghijklmnopqrstuvwxyz"
    elif strength == 0:
        characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    elif strength == 3:
        characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()"

    password = "".join(random.choice(characters) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    password_display_label.config(text="Generated Password: " + password)


def copy_to_clipboard():
    random_password = password_entry.get()
    pyperclip.copy(random_password)


# Main GUI
root = tk.Tk()
root.title("Password Generator")
root.configure(bg="#F0F0F0")

length_label = Label(root, text="Password Length:", background="#F0F0F0")
length_label.pack(pady=10)

length_var = IntVar()
length_combo = Combobox(root, textvariable=length_var)
length_combo["values"] = list(range(8, 33))
length_combo.current(0)
length_combo.pack()

strength_label = Label(root, text="Password Strength:", background="#F0F0F0")
strength_label.pack(pady=5)

strength_var = IntVar()
strength_radio_low = Radiobutton(
    root, text="Low", variable=strength_var, value=1)
strength_radio_medium = Radiobutton(
    root, text="Medium", variable=strength_var, value=0)
strength_radio_strong = Radiobutton(
    root, text="Strong", variable=strength_var, value=3)

strength_radio_low.pack(anchor="w", padx=30)
strength_radio_medium.pack(anchor="w", padx=30)
strength_radio_strong.pack(anchor="w", padx=30)

generate_button = Button(root, text="Generate Password",
                         command=generate_password)
generate_button.pack(pady=10)

password_entry = Entry(root, width=40)
password_entry.pack(pady=5)

copy_button = Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack(pady=5)

password_display_label = Label(root, text="", background="#F0F0F0")
password_display_label.pack(pady=10)

root.mainloop()
