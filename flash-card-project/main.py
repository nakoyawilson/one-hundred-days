from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- FLASH CARD DATA ------------------------------- #
try:
    words_data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    words_data = pandas.read_csv("data/french_words.csv")
all_words = words_data.French.to_list()
column_one_header = words_data.columns[0]
column_two_header = words_data.columns[1]
word_front = ""
word_back = ""


def select_word():
    global word_front, word_back, flip_timer
    window.after_cancel(flip_timer)
    canvas.itemconfig(flashcard, image=card_front_img)
    word_front = random.choice(all_words)
    canvas.itemconfig(title_text, text=column_one_header, fill="black")
    canvas.itemconfig(word_text, text=word_front, fill="black")

    # Get translation
    translation = words_data[words_data.French == word_front]
    word_back = translation.English.to_string(index=False)

    # Flip card
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(flashcard, image=card_back_img)
    canvas.itemconfig(title_text, text=column_two_header, fill="white")
    canvas.itemconfig(word_text, text=word_back, fill="white")


# ---------------------------- SAVE PROGRESS ------------------------------- #
def save_progress():
    if word_front == "":
        pass
    else:
        all_words.remove(word_front)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Vocabulary Flash Cards")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, flip_card)

card_back_img = PhotoImage(file="images/card_back.png")
card_front_img = PhotoImage(file="images/card_front.png")
right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
flashcard = canvas.create_image(400, 263, image=card_front_img)
title_text = canvas.create_text(400, 150, font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 263, font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

wrong_button = Button(image=wrong_img, highlightthickness=0, command=select_word)
wrong_button.grid(column=0, row=1)

right_button = Button(image=right_img, highlightthickness=0, command=lambda: [save_progress(), select_word()])
right_button.grid(column=1, row=1)

select_word()

window.mainloop()

# ---------------------------- CREATE WORDS TO LEARN CSV------------------------------- #
translated_words = [words_data.English[words_data.index[words_data.French == word][0]] for word in all_words]
data_dict = {
    "French": all_words,
    "English": translated_words
}
new_data = pandas.DataFrame(data_dict)
new_data.to_csv("data/words_to_learn.csv", index=False)
