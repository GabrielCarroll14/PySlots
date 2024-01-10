import tkinter as tk
import customtkinter
from customtkinter import CTkLabel, CTkEntry, CTkButton
import random
import sys

# Create the balance variable
balance = 100

# Create the settings for the window
root = customtkinter.CTk()
root.geometry("180x90")
customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")
root.title("PySlots")

# Create the bet function
def bet_func():
    
    # Turn the betamount and balance variables global
    global balance
    global betamount

    # Randomise the wheels
    spin1 = random.choice(["Cherry 🍒", "Orange 🍊", "Plum   🫐", "Bell   🔔", "Bar    🍫", "Seven   ❼"])
    spin2 = random.choice(["Cherry 🍒", "Orange 🍊", "Plum   🫐", "Bell   🔔", "Bar    🍫", "Seven   ❼"])
    spin3 = random.choice(["Cherry 🍒", "Orange 🍊", "Plum   🫐", "Bell   🔔", "Bar    🍫", "Seven   ❼"])

    # See if the user won or lost
    if spin1 == spin2 == spin3:
        balance = balance + betamount.get()
    else:
        balance = balance - betamount.get()

    # Run this if the user is in dept
    if balance < 1:
        losewin = customtkinter.CTk()
        losewin.geometry("250x50")
        losewin.title("Bankrupt")
        customtkinter.set_appearance_mode("light")
        customtkinter.set_default_color_theme("blue")
        loselabel = CTkLabel(losewin, text= "You are now bankrupt please try again.")
        loselabel.pack(padx=5, pady=5)
        losewin.mainloop()
        
        # exit the application
        sys.exit()
        
    # New window settings
    newwindow = customtkinter.CTk()
    newwindow.geometry("200x70")
    newwindow.title("Scores Window")
    customtkinter.set_appearance_mode("light")
    customtkinter.set_default_color_theme("blue")

    # Create the results label to display the results of the spin
    results = CTkLabel(newwindow, text=(spin1 + " " + spin2 + " " + spin3))
    results.pack(padx=5, pady=5)

    # Print out the user's current balance
    balance_label = CTkLabel(newwindow, text=("£" + str(balance)))
    balance_label.pack(padx=5, pady=5)

    # create the main loop to keep the app running
    newwindow.mainloop()

# Create the text box for the user to input the amount they want to bet
betamount = tk.IntVar()
bet_amount_box = CTkEntry(root, width=150, textvariable=betamount)
bet_amount_box.pack(padx=5, pady=5)

# Create a button to initiate the bet
bet_button = CTkButton(root, text="Bet!", command=bet_func, corner_radius=100)
bet_button.pack(padx=3, pady=3)

# Create the main loop to keep the app running
root.mainloop()