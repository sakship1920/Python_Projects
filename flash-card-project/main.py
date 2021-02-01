import pandas
import random
from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/german_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records") # orient helps to ma make dictionery in proper way


# ------------------------ BUTTONS---------------------------
def next_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="German", fill="black")
    canvas.itemconfig(card_word, text=current_card["German"],fill="black")
    canvas.itemconfig(card_background, image=flash_front_image)
    flip_timer = window.after(3000, func=flip_card)

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_word()

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white") # fill is use to change text color
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=flash_back_image)



# ------------------------ USER UI---------------------------
window = Tk()
window.title("Flash Card!")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer= window.after(3000, func=flip_card)


canvas = Canvas(width=800, height=526)
flash_front_image= PhotoImage(file="images/card_front.png")
flash_back_image= PhotoImage(file="images/card_back.png")
card_background= canvas.create_image(400, 263, image=flash_front_image)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_title=canvas.create_text(400, 150, text="",font=("Arieal", 30, "italic"))
card_word = canvas.create_text(400, 263, text="",font=("Arieal", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)



# Buttons
wrong_btn_img = PhotoImage(file="images/wrong.png")
wrong_btn = Button(image=wrong_btn_img, highlightthickness=0, command=next_word)
wrong_btn.grid(row=1, column=0)

right_btn_img = PhotoImage(file="images/right.png")
right_btn = Button(image=right_btn_img, highlightthickness=0, command=is_known)
right_btn.grid(row=1, column=1)


next_word()
window.mainloop()

