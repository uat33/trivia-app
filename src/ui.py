from tkinter import * # import tkinter
from quiz_brain import QuizBrain # import the quiz brain class

THEME_COLOR = "#375362" # set this is as a constant
# can easily change color if we want to now



class QuizInterface:
    """
        This class handles the UI for the quiz.
    """
    def __init__(self, quiz_brain: QuizBrain):
        """
            Initializes a variety of attributes.

            - quiz to access the quiz_brain which has the logic
            - window which will be the Tkinter()
            - score which will be the label that shows the users score
            - canvas which will contain the question
            - true which will be the true button
            - false which will be the false button
            - text which will contain the question text
        """
        # initialize everything
        self.quiz = quiz_brain 
        self.window = Tk()
        self.window.title("Trivia!") # title the window
        self.window.config(bg=THEME_COLOR, padx=20, pady=20) # space things out so it looks nicer
        
        # the label which will tell the user what their score is
        self.score = Label(text=f"Score: { self.quiz.score}", bg=THEME_COLOR, fg='white')
        # grid it in the top right
        self.score.grid(column=1, row=0)

        # make a canvas wide nough to hold the questions
        # give it the appropriate dimensions
        # grid it in the center
        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=25)

        # get the images for the true and false buttons
        # don't need self. because we won't use anywhere else
        correct_image = PhotoImage(file="images/true.png")
        wrong_image = PhotoImage(file="images/false.png")

        # create the true and false buttons and link those to their respective function using the command attribute
        self.true = Button(image=correct_image, highlightbackground=THEME_COLOR, command=self.true_press)
        self.false = Button(image=wrong_image, highlightbackground=THEME_COLOR, command=self.false_press)
        # grid them in their locations
        self.true.grid(column=1, row=2) 
        self.false.grid(column=0, row=2)

        # create the text variable which will house the question text
        self.text = self.canvas.create_text(150, 125, width='260', text="",
                                font=("Arial", 20, 'italic'), fill=THEME_COLOR)
        # call get_next_question which will set up the next question 
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        """
        This function takes care of getting the questions.
        
        """

        # if there are no more questions
        if not self.quiz.still_has_question():
            # tell the user the quiz is over
            # give them their score
            self.canvas.itemconfig(self.text, text=f"Quiz complete\nYour score is {self.quiz.score} / {len(self.quiz.questions_list)}")

            # disable the true and false buttons so they can't click them forever
            self.true.config(state='disabled')
            self.false.config(state='disabled')

        # give the canvas a white background again as it will have changed colors after the user answered
        self.canvas.config(bg='white')
        # update the score
        self.score.config(text=f"Score: {self.quiz.score}")
        # save the next questions text in a variable
        q_text = self.quiz.next_question()
        # update the canvas so that the text element shows the new text
        self.canvas.itemconfig(self.text, text=q_text)


    def true_press(self):
        """
            This method is called if the user guesses true.
        """
        # call the check answer method in the quiz brain with True which was the user's guess
        # pass the boolean value that returns into the give feedback function
        self.give_feedback(self.quiz.check_answer("True"))
    
    def false_press(self):
        """
            This method is called if the user guesses false.
        """
        # call the check answer method in the quiz brain with False which was the user's guess
        # pass the boolean value that returns into the give feedback function
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        """
            This method tells the user whether they got the question correct or not.
        """
        if is_right: # if they got it right
            self.canvas.config(bg="green") # turn the canvas green
        else: # otherwise
            self.canvas.config(bg="red") # turn the canvas red
        self.window.after(1000, self.get_next_question) # wait a second, then get the next question
    

