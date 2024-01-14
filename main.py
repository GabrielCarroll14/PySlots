import tkinter as tk
import customtkinter
from customtkinter import CTkLabel, CTkEntry, CTkButton
import random
import sys

# Create the balance and username variable
balance = 100
user_name = ""

# Create the settings for the window
root = customtkinter.CTk()
root.geometry("180x150")
customtkinter.set_appearance_mode("system") # The user may ajust this to "light" or "dark" mode depending on their preferences 
customtkinter.set_default_color_theme("blue")
root.title("PySlots")
root.iconbitmap("icon.ico")

def read_scores():
    
    with open ("scores.txt", "r") as a:
        content = a.read()

    # Window settings
    readwindow = customtkinter.CTk()
    readwindow.geometry("200x70")
    customtkinter.set_appearance_mode("system")  # The user may ajust this to "light" or "dark" mode depending on their preferences 
    customtkinter.set_default_color_theme("blue")
    readwindow.title("PySlots")
    readwindow.iconbitmap("icon.ico")
    
    scores = CTkLabel(readwindow, text = (str(content)))
    scores.pack(pady=5, padx=5)
    
    readwindow.mainloop()

# Create the save score window function
def save_score_window():
    
    # Declare balance and user_name global
    global balance
    global user_name
    
    # Window settings
    savewindow = customtkinter.CTk()
    savewindow.geometry("200x70")
    customtkinter.set_appearance_mode("system") # The user may ajust this to "light" or "dark" mode depending on their preferences 
    customtkinter.set_default_color_theme("blue")
    savewindow.title("PySlots")
    savewindow.iconbitmap("icon.ico")
    
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
    
    # Declare balance and user_name global
    global user_name
    global balance
    
    # Write the data to a file
    with open ("scores.txt", "a") as f:
        f.write("Username: " + user_name.get() + " Score: £" + str(balance) + "\n")

# Create the bet function
def bet_func():
    
    # Turn the betamount and balance variables global
    global balance
    global betamount
    
    # Give the user an error if they bet over £100
    if betamount.get() > 100:
        
        # Window settings
        overwin = customtkinter.CTk()
        overwin.geometry("170x30")
        customtkinter.set_appearance_mode("system") # The user may ajust this to "light" or "dark" mode depending on their preferences 
        customtkinter.set_default_color_theme("blue")
        overwin.title("PySlots")
        overwin.iconbitmap("icon.ico")
        
        # Display the message in a label
        erroramount = CTkLabel(overwin, text= "Please bet under £100")
        erroramount.pack(padx=5, pady=5)
        
        # Create the mainloop
        overwin.mainloop()
        
    # Run the correct code if the user bets a correct amount
    elif betamount.get() <= 100:

        # Randomise the wheels
        spin1 = random.choice(["Cherry 🍒", "Orange 🍊", "Plum   🫐", "Bell   🔔", "Bar    🍫", "Seven   ❼"])
        spin2 = random.choice(["Cherry 🍒", "Orange 🍊", "Plum   🫐", "Bell   🔔", "Bar    🍫", "Seven   ❼"])
        spin3 = random.choice(["Cherry 🍒", "Orange 🍊", "Plum   🫐", "Bell   🔔", "Bar    🍫", "Seven   ❼"])

        # Return the user their bet if they won
        if spin1 == spin2 == spin3:
            balance = balance + betamount.get()
    
        # Return the user half their bet if they got two matching symbols
        elif spin1 == spin2 or spin2 == spin3 or spin1 == spin3:
            half_betamount = betamount.get() / 2
            balance = balance + half_betamount
    
        # Minus the users bet from their balance if they got none correct    
        else:
            balance = balance - betamount.get()

        # Run this if the user is in dept
        if balance < 1:
        
            # Create the window if the user is in dept
            losewin = customtkinter.CTk()
            losewin.geometry("250x50")
            losewin.title("PySlots")
            customtkinter.set_appearance_mode("system") # The user may ajust this to "light" or "dark" mode depending on their preferences 
            customtkinter.set_default_color_theme("blue")
            loselabel = CTkLabel(losewin, text= "You are now bankrupt please try again.")
            loselabel.pack(padx=5, pady=5)
            losewin.mainloop()
            losewin.iconbitmap("icon.ico")
        
            # exit the application
            sys.exit()
        
        # newwindow settings
        newwindow = customtkinter.CTk()
        newwindow.geometry("200x70")
        newwindow.title("PySlots")
        customtkinter.set_appearance_mode("system") # The user may ajust this to "light" or "dark" mode depending on their preferences 
        customtkinter.set_default_color_theme("blue")
        newwindow.iconbitmap("icon.ico")

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

# Create the save score button
save_score_button = CTkButton(root, text="Save Score", corner_radius=100, command=save_score_window)
save_score_button.pack(padx=5, pady=5)

# Create a read scores button
read_button = CTkButton(root, text="View", command=read_scores, corner_radius=100)
read_button.pack(padx=5,pady=5)

# Create the main loop to keep the app running
root.mainloop()