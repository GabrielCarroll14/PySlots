# Import stuffs
import tkinter as tk
import customtkinter
from customtkinter import CTkLabel, CTkEntry, CTkButton
import random
import sys

# Create the balance variable
balance = 100

# Create the settings for the window
root = customtkinter.CTk()
root.geometry("180x117")
customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")
root.title("PySlots")

# Create the save score window function
def save_score_window():
    
    # Declare balance and user_name global
    global balance
    global user_name
    
    # Window settings
    savewindow = customtkinter.CTk()
    savewindow.geometry("200x70")
    customtkinter.set_appearance_mode("light")
    customtkinter.set_default_color_theme("blue")
    savewindow.title("Save")
    
    # Prompt the user to enter their user name
    user_name = tk.StringVar()
    name_box = CTkEntry(savewindow, height=10, width=300, textvariable=user_name)
    name_box.pack(padx=5, pady=5)
    
    # Get the user to save thier username
    save_button = CTkButton(savewindow, text= "save", command=filewrite )
    save_button.pack(padx=5, pady=5)
    
    # Create the mainloop
    savewindow.mainloop()

# Create the filewrite func to save data to the scores.txt file    
def filewrite():
    global user_name
    with open ("scores.txt", "a") as f:
        f.write("Username: " + user_name.get() + " Score £" + str(balance) + "\n")

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

save_score_button = CTkButton(root, text="Save Score", corner_radius=100, command=save_score_window)
save_score_button.pack(padx=5, pady=5)

# Create the main loop to keep the app running
root.mainloop()