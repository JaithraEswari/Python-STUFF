from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250,
                             bg='white', highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150, 125, width=280, font=("Arial", 15, 'italic'))
        self.canvas.grid(column=0, row=1, columnspan=2, padx=20, pady=20)

        self.score_label = Label(text='score:0', bg=THEME_COLOR, fg='white')
        self.score_label.grid(column=1, row=0)

        self.right_image = PhotoImage(file='./images/true.png')
        self.wrong_image = PhotoImage(file='./images/false.png')

        self.rightbutton = Button(image=self.wrong_image,
                             highlightthickness=0, command=self.wrong_answer)
        self.rightbutton.grid(column=0, row=2, padx=20, pady=20)

        self.wrongbutton = Button(image=self.right_image,
                             highlightthickness=0, command=self.right_answer)
        self.wrongbutton.grid(column=1, row=2, padx=20, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_label.config(text=f'score: {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've completed the quiz")
            self.rightbutton.config(state='disabled')
            self.wrongbutton.config(state='disabled')

    def right_answer(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def wrong_answer(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)
