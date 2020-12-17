from tkinter import *
import random
import pandas   as pd
import time

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- WORD GENERATOR ------------------------------- #
try:
    data = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("./data/french_words.csv")
    to_learn = data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

current_card = {}

def new_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer) # cancel existing flip_timer
    current_card = random.choice(to_learn)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=f"{current_card['French']}", fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card) # recreate flip_timer and start counting for 3 sec

def flip_card():
    global current_card
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=f"{current_card['English']}", fill="white")
    canvas.itemconfig(card_background, image=card_back_img)

def know_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("./data/words_to_learn.csv", index=False)
    current_card = random.choice(to_learn)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=f"{current_card['French']}", fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(height=526, width=800)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)
title_text = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

cross_img = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=cross_img, highlightthickness=0, command=new_card)
wrong_button.grid(row=1, column=0)

tick_img = PhotoImage(file="./images/right.png")
right_button = Button(image=tick_img, highlightthickness=0, command=know_card)
right_button.grid(row=1, column=1)

new_card()

window.mainloop()