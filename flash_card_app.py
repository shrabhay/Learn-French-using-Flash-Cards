from tkinter import *
import pandas
import random
import os

os.system('clear')

BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ('Ariel', 40, 'italic')
WORD_FONT = ('Ariel', 60, 'bold')

random_word = {}
french_words_list = []

try:
    french_words_df = pandas.read_csv('data/words_left_to_learn.csv')
except FileNotFoundError:
    original_french_words_df = pandas.read_csv('data/french_words.csv')
    french_words_list = original_french_words_df.to_dict(orient='records')
else:
    french_words_list = french_words_df.to_dict(orient='records')


def next_word():
    global random_word, flip_timer
    window.after_cancel(flip_timer)

    random_word = random.choice(french_words_list)
    canvas.itemconfig(flash_card_image, image=flash_card_front_image)
    canvas.itemconfig(flash_card_title, text='French', fill='black')
    canvas.itemconfig(flash_card_word, text=random_word['French'], fill='black')

    flip_timer = window.after(3000, func=flip_card)


def is_known():
    french_words_list.remove(random_word)
    words_left_to_learn_list = pandas.DataFrame(french_words_list)
    words_left_to_learn_list.to_csv('data/words_left_to_learn.csv', index=False)
    next_word()


def flip_card():
    canvas.itemconfig(flash_card_image, image=flash_card_back_image)
    canvas.itemconfig(flash_card_title, text='English', fill='white')
    canvas.itemconfig(flash_card_word, text=random_word['English'], fill='white')


window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
flash_card_front_image = PhotoImage(file='images/card_front.png')
flash_card_back_image = PhotoImage(file='images/card_back.png')
flash_card_image = canvas.create_image(403, 265, image=flash_card_front_image)
canvas.grid(column=0, row=0, columnspan=2)

flash_card_title = canvas.create_text(400, 150, text='', font=TITLE_FONT)
flash_card_word = canvas.create_text(400, 263, text='', font=WORD_FONT)

unknown_button_image = PhotoImage(file='images/wrong.png')
unknown_button = Button(image=unknown_button_image, highlightbackground=BACKGROUND_COLOR, highlightthickness=0,
                        command=next_word)
unknown_button.grid(column=0, row=1)

known_button_image = PhotoImage(file='images/right.png')
known_button = Button(image=known_button_image, highlightbackground=BACKGROUND_COLOR, highlightthickness=0,
                      command=is_known)
known_button.grid(column=1, row=1)

next_word()

window.mainloop()
