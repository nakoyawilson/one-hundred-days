from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.score_text = Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=("Arial", 15))
        self.score_text.grid(column=1, row=0, sticky=E)
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Quiz questions here", font=FONT,
                                                     fill=THEME_COLOR, justify="center")
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.true_selected)
        self.true_button.grid(column=0, row=2)
        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.false_selected)
        self.false_button.grid(column=1, row=2)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.score_text.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,
                                   text=f"You've reached the end of the quiz.\n\nYou got {self.quiz.score} out of {len(self.quiz.question_list)} questions correct!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_selected(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_selected(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
