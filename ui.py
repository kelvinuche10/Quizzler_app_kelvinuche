from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.score = 0
        self.window.title('Quizzler')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text='Score = 0', fg='white', bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(height=250, width=300, bg='white')
        self.question_label = self.canvas.create_text(150,
                                                      125,
                                                      fill=THEME_COLOR,

                                                      width=280,
                                                      text='Some Question first',
                                                      font=('Arial', 20, 'italic'))

        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        false_image = PhotoImage(file='images\\false.png')
        true_image = PhotoImage(file='images\\true.png')
        self.false = Button(image=false_image, highlightthickness=0, borderwidth=0)
        self.false.grid(row=2, column=1)
        self.true = Button(image=true_image, highlightthickness=0, borderwidth=0)
        self.true.grid(row=2, column=0)
        self.get_question()

        self.window.mainloop()

    def get_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score {self.quiz.score}")
            q_text = self.quiz.next_question
            self.canvas.itemconfig(self.question_label, text=q_text)
        else:
            self.canvas.itemconfig(self.question_label, text='You have reached the end of the quiz.')
            self.true.config(state='disabled')
            self.false.config(state='disabled')

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer('True'))


    def false_pressed(self):
        is_right = self.quiz.check_answer('False')
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, func=self.get_question)


