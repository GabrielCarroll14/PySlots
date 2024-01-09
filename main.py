import tkinter as tk
import customtkinter
from customtkinter import *
from customtkinter import CTkLabel, CTkEntry, CTkButton
import random

# Create the balance variable
balance = 100

# Create the settings for the window
root = customtkinter.CTk()
root.geometry("180x90")
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")
root.title("PySlots")

def bet_func():
    global balance
    global betamount

    # Randomise the wheels
    spin1 = random.choice(["Cherry 🍒", "Orange 🍊", "Plum   🫐", "Bell   🔔", "Bar    🍫", "Seven   ❼"])
    spin2 = random.choice(["Cherry 🍒", "Orange 🍊", "Plum   🫐", "Bell   🔔", "Bar    🍫", "Seven   ❼"])
    spin3 = random.choice(["Cherry 🍒", "Orange 🍊", "Plum   🫐", "Bell   🔔", "Bar    🍫", "Seven   ❼"])

    if spin1 == spin2 == spin3:
        balance = balance + betamount.get()
    else:
        balance = balance - betamount.get()

    # New window settings
    newwindow = customtkinter.CTk()
    newwindow.geometry("200x70")
    newwindow.title("Scores Window")
    customtkinter.set_appearance_mode("system")
    customtkinter.set_default_color_theme("blue")

    # Create the results label to display the results of the spin
    results = CTkLabel(newwindow, text=(spin1 + " " + spin2 + " " + spin3))
    results.pack(padx=5, pady=5)

    # Print out the user's current balance
    balance_label = CTkLabel(newwindow, text=("£" + str(balance)))
    balance_label.pack(padx=5, pady=5)

    newwindow.mainloop()

# Create the text box for the user to input the amount they want to bet
betamount = tk.IntVar()
bet_amount_box = CTkEntry(root, width=150, textvariable=betamount)
bet_amount_box.pack(padx=5, pady=5)

# Create a button to initiate the bet
bet_button = CTkButton(root, text="Bet!", command=bet_func)
bet_button.pack(padx=3, pady=3)

# Create the main loop to keep the app running
root.mainloop()

