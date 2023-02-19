import tkinter as tk
from tkinter import font
import random

# Create the root window
root = tk.Tk()
root.geometry("500x200")

# Define the list of Bible proverbs
bible_proverbs = [
    "Trust in the Lord with all your heart and lean\n not on your own understanding. In all your ways submit to him,\n and he will make your paths straight.\n - Proverbs 3:5-6",
    "A gentle answer turns away wrath, but a harsh word\n stirs up anger.\n - Proverbs 15:1",
    "The fear of the Lord is the beginning of wisdom, and knowledge of the Holy One is understanding. - Proverbs 9:10",
    "Better is a little with the fear of the Lord than\n great wealth with turmoil.\n - Proverbs 15:16",
    "The tongue has the power of life and death, and\n those who love it will eat its fruit.\n - Proverbs 18:21",
    "A righteous man walks in his integrity;\n his children are blessed after him.\n - Proverbs 20:7",
    "Do not be wise in your own eyes;\n fear the Lord and shun evil.\n - Proverbs 3:7",
    "The plans of the diligent lead to profit as surely\n as haste leads to poverty.\n - Proverbs 21:5",
    "Kind words are like honey—sweet\n to the soul and healthy for the body.\n - Proverbs 16:24",
    "He who gets wisdom loves his own soul;\n he who cherishes understanding prospers.\n - Proverbs 19:8",
    "Commit to the Lord whatever you do,\n and your plans will succeed.\n - Proverbs 16:3",
    "The eyes of the Lord are everywhere,\n keeping watch on the wicked and the good.\n - Proverbs 15:3",
    "A man’s heart plans his way,\n but the Lord determines his steps.\n - Proverbs 16:9",
    "The wicked flee though no one pursues,\n but the righteous are as bold as a lion.\n - Proverbs 28:1",
    "A soft answer turns away wrath,\n but a harsh word stirs up anger.\n - Proverbs 15:1",
    "The wise in heart are called discerning,\n and pleasant words promote instruction.\n - Proverbs 16:21",
    "The way of the lazy man is like a hedge of thorns,\n but the path of the upright is a highway.\n - Proverbs 15:19",
    "The fear of the Lord is the beginning of knowledge,\n but fools despise wisdom and discipline.\n - Proverbs 1:7",
    "A wise son brings joy to his father,\n but a foolish man despises his mother.\n - Proverbs 15:20",
    "A friend loves at all times,\n and a brother is born for a time of adversity.\n - Proverbs 17:17",
]

# Create the button
def display_proverb():
    # Choose a random proverb from the list
    proverb = random.choice(bible_proverbs)
    # Update the label with the chosen proverb
    label.config(text=proverb)

button = tk.Button(root, text="Display Proverb", command=display_proverb)
button.pack(pady=20)

# Create the label
fancy_font = font.Font(family="Comic Sans MS", size=12, weight="bold")
label = tk.Label(root, text="", font=fancy_font)
label.pack()

# Start the main event loop
root.mainloop()