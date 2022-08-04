import tkinter
BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_TEXT = ('Ariel', 40, 'italic')
WORD_TEXT = ('Ariel', 70, 'bold')

window = tkinter.Tk()
window.title('Multilingo - Learn French The Easy Way')
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)


canvas = tkinter.Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
flash_card_front = tkinter.PhotoImage(file='./images/card_front.png')
canvas.create_image(400, 275, image=flash_card_front)
flash_card_language_text = canvas.create_text(380, 150, text='In English', fill='black', font=LANGUAGE_TEXT)
flash_card_word_text = canvas.create_text(380, 293, text='Word', fill='black', font=WORD_TEXT)
canvas.grid(column=0, row=0, columnspan=2)


x_button_img = tkinter.PhotoImage(file='./images/wrong.png')
x_button = tkinter.Button(image=x_button_img, highlightthickness=0)
x_button.grid(column=0, row=1)


checkmark_button_img = tkinter.PhotoImage(file='./images/right.png')
checkmark_button = tkinter.Button(image=checkmark_button_img, highlightthickness=0)
checkmark_button.grid(column=1, row=1)





window.mainloop()

