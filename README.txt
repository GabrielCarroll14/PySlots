# PySlots

PySlots is a simple slot machine game implemented in Python using the Tkinter library. Users can place bets, spin the wheels, and view or save their scores.

## Features

- **Betting:** Users can input the amount they want to bet using the provided entry box.

- **Spinning Wheels:** The slot machine wheels are randomly spun, and the results are displayed.

- **Winning Rules:**
  - If all three symbols match, the user's balance increases by the bet amount.
  - If two symbols match, the user receives half of their bet amount.
  - If no symbols match, the bet amount is deducted from the user's balance.

- **Saving Scores:** Users can save their username and current score to a file by clicking the "Save Score" button.

- **Viewing Scores:** Users can view saved scores by clicking the "View" button, which opens a new window displaying the scores from the scores.txt file.

- **Bankruptcy:** If the user's balance goes below 1, they are declared bankrupt, and the application exits.

## Customization

- **Appearance Mode:** Users can adjust the appearance mode to "light" or "dark" mode based on their preferences.

- **Color Theme:** The color theme for the application can be changed. The default is set to "dark-blue."

## Sound Effects

- Sound effects are used to enhance the gaming experience. The `winsound` library is utilized for playing audio files.

## File Structure

- `pyslots.py`: The main Python script containing the PySlots game implementation.
- `scores.txt`: A text file where user scores are saved.

## Acknowledgments

- PySlots uses the Tkinter library for the graphical user interface.

Feel free to customize and improve upon this simple slot machine game!
