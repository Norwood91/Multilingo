import tkinter
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_TEXT = ('Ariel', 30, 'italic')
RULE_TEXT = ('Ariel', 10, 'italic')
WORD_TEXT = ('Ariel', 85, 'bold')
current_card = {}
to_study = {}

try:
    data = pandas.read_csv('data/words_to_study.csv')
except FileNotFoundError:
    original_data = pandas.read_csv('data/french_words.csv')
    to_study = original_data.to_dict(orient='records')
else:
    to_study = data.to_dict(orient='records')



def next_card():
    global current_card, flip_timer
    # Cancel timer before next card
    window.after_cancel(flip_timer)
    current_card = random.choice(to_study)
    canvas.itemconfig(flash_card_language_text, text='What does this French word\nmean in English:', fill='black')
    canvas.itemconfig(flash_card_word_text, text=current_card['French'].capitalize(), fill='black')
    canvas.itemconfig(flash_card_background, image=flash_card_front)
    # After your next card is loaded, start timer
    flip_timer = window.after(20000, func=flip_card)


def flip_card():
    canvas.itemconfig(flash_card_language_text, text='In English:')
    canvas.itemconfig(flash_card_word_text, text=current_card['English'].capitalize(), fill='white')
    canvas.itemconfig(flash_card_background, image=flash_card_back)

def guessed_word_correctly():
    # Removes the current card from the list of data
    to_study.remove(current_card)
    data = pandas.DataFrame(to_study)
    data.to_csv('data/words_to_study.csv', index=False)
    next_card()


window = tkinter.Tk()
window.title('Multilingo - Learn French The FUN Way')
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(20000, func=flip_card)

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
                                          text='Click the green button if you guessed correct (this\'ll remove it from the deck)'
                                               '\nand the red button if you guessed wrong (this\'ll keep it in deck for further studying)\n'
                                               'You have 20 seconds to guess the translation of the word!',
                                          fill='black',
                                          font=RULE_TEXT
                                          )

x_button_img = tkinter.PhotoImage(file='./images/wrong.png')
x_button = tkinter.Button(image=x_button_img, highlightthickness=0, command=next_card)
x_button.grid(column=0, row=1)

checkmark_button_img = tkinter.PhotoImage(file='./images/right.png')
checkmark_button = tkinter.Button(image=checkmark_button_img, highlightthickness=0, command=guessed_word_correctly)
checkmark_button.grid(column=1, row=1)

next_card()

window.mainloop()
