import tkinter
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_TEXT = ('Ariel', 30, 'italic')
RULE_TEXT = ('Ariel', 12, 'italic')
WORD_TEXT = ('Ariel', 85, 'bold')

data = pandas.read_csv('data/french_words.csv')
data_dict = data.to_dict(orient='records')
current_card = {}


def next_card():
    global current_card, flip_timer
    # Cancel timer before next card
    window.after_cancel(flip_timer)
    current_card = random.choice(data_dict)
    canvas.itemconfig(flash_card_language_text, text='What does this French word\nmean in English:', fill='black')
    canvas.itemconfig(flash_card_word_text, text=current_card['French'].capitalize(), fill='black')
    canvas.itemconfig(flash_card_background, image=flash_card_front)
    # After your next card is loaded, start timer
    flip_timer = window.after(10000, func=flip_card)


def flip_card():
    canvas.itemconfig(flash_card_language_text, text='In English:')
    canvas.itemconfig(flash_card_word_text, text=current_card['English'].capitalize(), fill='white')
    canvas.itemconfig(flash_card_background, image=flash_card_back)


window = tkinter.Tk()
window.title('Multilingo - Learn French The FUN Way')
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(10000, func=flip_card)

canvas = tkinter.Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
flash_card_front = tkinter.PhotoImage(file='./images/card_front.png')
flash_card_back = tkinter.PhotoImage(file='./images/card_back.png')
flash_card_background = canvas.create_image(400, 275, image=flash_card_front)
flash_card_language_text = canvas.create_text(380, 150,
                                              text='What does this French word\nmean in English:',
                                              fill='black', font=LANGUAGE_TEXT)

flash_card_word_text = canvas.create_text(380, 300, fill='black', font=WORD_TEXT)
canvas.grid(column=0, row=0, columnspan=2)

flash_card_rule_text = canvas.create_text(380, 450,
                                      text='Click the green button if you guessed correct,\n and the red button if you '
                                           'guessed wrong. You\n have 10 seconds to guess!',
                                      fill='black',
                                      font=RULE_TEXT
                                      )

x_button_img = tkinter.PhotoImage(file='./images/wrong.png')
x_button = tkinter.Button(image=x_button_img, highlightthickness=0, command=next_card)
x_button.grid(column=0, row=1)


checkmark_button_img = tkinter.PhotoImage(file='./images/right.png')
checkmark_button = tkinter.Button(image=checkmark_button_img, highlightthickness=0, command=next_card)
checkmark_button.grid(column=1, row=1)

next_card()

window.mainloop()
