from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")

class QuizInterface():
    # add quiz brain & it's data type as a param
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz app demo")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        # score txt
        self.score_txt = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_txt.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0, bg="white")
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Questions go here!!",
                                                     fill=THEME_COLOR, font=FONT)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        # buttons
        right_img = PhotoImage(file="./images/true.png")
        right_btn = Button(image=right_img, highlightthickness=0)
        right_btn.grid(row=3, column=0)

        left_img = PhotoImage(file="./images/false.png")
        left_btn = Button(image=left_img, highlightthickness=0)
        left_btn.grid(row=3, column=1)


        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)