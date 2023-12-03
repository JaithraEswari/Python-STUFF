import tkinter as tk
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"
word = {}
to_learn = {}

try:
    data_dict = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("./data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data_dict.to_dict(orient="records")







def random_word_f():
        global word, flip_timer
        windows.after_cancel(flip_timer)
        word = random.choice(to_learn)
        canvas.itemconfig(word_text, text=word["French"], fill= "black")
        canvas.itemconfig(canvas_image, image=card_image_f)
        canvas.itemconfig(title, text="French", fill= "black")
        flip_timer = windows.after(3000, random_word_e)

        
def random_word_e(): 
        
        canvas.itemconfig(word_text, text=word["English"], fill= "white")
        canvas.itemconfig(canvas_image, image=card_image_e)
        canvas.itemconfig(title, text="English", fill= "white")

def is_known():
        to_learn.remove(word)
        data = pd.DataFrame(to_learn)
        data.to_csv("./data/words_to_learn.csv", index=False)
        random_word_f()

# ---------------------------- UI SETUP ------------------------------- #
windows = tk.Tk()
windows.title("Flash Card")
windows.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = windows.after(3000, random_word_e)


canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_image_f = tk.PhotoImage(file="./images/card_front.png")
card_image_e = tk.PhotoImage(file="./images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_image_f)
title = canvas.create_text(400, 150, text="French", font=("Arial",40, "italic"))
word_text = canvas.create_text(400, 263, text="word", font=("Arial",60, "bold"))
canvas.grid(column=0, row=1, columnspan=2)

wrong_image = tk.PhotoImage(file="./images/wrong.png")
button = tk.Button(image=wrong_image, highlightthickness=0, command=random_word_f)
button.grid(column=0, row=2)

right_image = tk.PhotoImage(file="./images/right.png")
button = tk.Button(image=right_image, highlightthickness=0, command=is_known)
button.grid(column=1, row=2)

random_word_f()


windows.mainloop()