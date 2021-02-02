from tkinter import *
from PIL import Image, ImageTk
from quiz_app import QuizBrain

# "#83a95c"
TRUE_COLOR = "#295939"
FALSE_COLOR = "#ff4646"
BUTTON_FONT = ("Arial", "13", "bold")
THEME_COLOR =  "#2c061f"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        # Creating a new window,size,title,setting resizable to 0
        self.window = Tk()
        self.window.geometry("340x430")
        self.window.title("Quiz App")
        self.window.resizable(0, 0)
        self.window.config(bg=THEME_COLOR)

        # Quiz App title
        self.app_title = Label()
        self.app_title.config(text="Quiz App", font=("Arial", 20, "bold"), bg=THEME_COLOR, fg="white")
        self.app_title.grid(row=0, column=0, columnspan=2, pady=20)

        # canvas
        self.canvas = Canvas(width=335, height=150)
        self.question_text = self.canvas.create_text(
            170,
            75,
            width=300,
            text="",
            font=("Times New Roman", 18, "normal"),
        )
        self.canvas.config(bg="#fdffbc")
        self.canvas.grid(row=1, column=0, columnspan=2)

        # button -----> TRUE and FALSE
        self.true_button = Button()
        self.true_button.config(text="True", bg=TRUE_COLOR, fg="white", font=BUTTON_FONT)
        self.true_button.config(command=lambda: self.check_answer("True"))
        self.true_button.grid(row=3, column=0, sticky="WE")

        self.false_button = Button()
        self.false_button.config(text="False", bg=FALSE_COLOR, font=BUTTON_FONT)
        self.false_button.config(command=lambda: self.check_answer("False"))
        self.false_button.grid(row=3, column=1,  sticky="WE")

        # Quit button
        self.quit_button = Button()
        self.quit_button.config(text="Quit", width=16, font=BUTTON_FONT)
        self.quit_button.config(command=self.window.destroy)
        self.current_score = f"{self.quiz.score} / {self.quiz.current_question_number}"
        self.next_question()
        self.window.mainloop()

    def next_question(self):
        if self.quiz.still_has_question():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.activate_buttons()
        else:
            img.grid_remove()
            self.canvas.itemconfig(self.question_text, text=f"\tQuiz Over \n\n Final Score  : {self.current_score}")
            self.deactivate_buttons()
            self.quit_button.grid(row=4, column=0, columnspan=2, pady=20)

    def display_logo(self, answer):
        load_image = Image.open(f"images/{answer}.png")
        render_image = ImageTk.PhotoImage(load_image)
        global img
        img = Label(image=render_image)
        img.image = render_image
        img.grid(row=4, column=0, columnspan=2, pady=20)


    def check_answer(self, user_answer):
        correct_answer = self.quiz.check_answer(user_answer)
        self.current_score = f"{self.quiz.score} / {self.quiz.current_question_number}"
        if correct_answer:
            self.display_logo("thumb-up")
            self.canvas.itemconfig(self.question_text, text=f" That's Right \n\n Score : {self.current_score}")
        else:
            self.display_logo("thumb-down")
            self.canvas.itemconfig(self.question_text, text=f" That's Wrong \n\n Score : {self.current_score}")


        self.refresh()

    def refresh(self):
        self.deactivate_buttons()
        self.window.after(1500, img.grid_remove)
        self.window.after(1500, self.next_question)

    def deactivate_buttons(self):
        self.true_button.config(state=DISABLED)
        self.false_button.config(state=DISABLED)

    def activate_buttons(self):
        self.true_button.config(state=NORMAL)
        self.false_button.config(state=NORMAL)