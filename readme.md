**Welcome to the U.S. States Game README!**

This game challenges you to guess the names of all 50 U.S. states. It utilizes Python's `pandas` and `turtle` libraries to interact with a CSV file containing state information and display the game on a screen.

**Dependencies:**

- `pandas` (install with `pip install pandas`)
- `turtle` (comes pre-installed with most Python distributions)

**How to Play:**

1. Ensure you have the `50_states.csv` file containing state names and coordinates in the same directory as this Python script.
2. Run the script: `python main.py`

**Gameplay:**

- The game starts by displaying a map of the U.S. states as a background image.
- You'll be prompted to enter the name of a state (case-insensitive).
- If you guess a state correctly:
    - The state name will be written on the map at its corresponding location.
    - The state will be added to the list of correctly guessed states.
- If you enter "Exit", the game will end and list the remaining states you haven't guessed in a CSV file named `states_to_lean.csv`.
- The game continues until you guess all 50 states or choose to exit.

