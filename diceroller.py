import tkinter as tk
import random

# Create main window
root = tk.Tk()
root.title("Dice Rolling Game 🎲")
root.geometry("300x300")
root.resizable(False, False)

# Dice emojis
dice_faces = {
    1: "⚀",
    2: "⚁",
    3: "⚂",
    4: "⚃",
    5: "⚄",
    6: "⚅"
}

# Function to roll dice
def roll_dice():
    result = random.randint(1, 6)
    label.config(text=f"{dice_faces[result]}  ({result})")

# Title label
title = tk.Label(root, text="Roll the Dice!", font=("Arial", 18))
title.pack(pady=20)

# Result label
label = tk.Label(root, text="🎲", font=("Arial", 80))
label.pack()

# Roll button
roll_button = tk.Button(root, text="Roll Dice", command=roll_dice, font=("Arial", 14))
roll_button.pack(pady=20)

# Run app
root.mainloop()