from data import question_data # get the question data from the data file
from question_model import Question # get the question class
from quiz_brain import QuizBrain # get the QuizBrain class
from ui import QuizInterface # get the QuizInterface class
from html import unescape # get the unescape method

# create the question bank that we will get our questions from
# first use html.unescape so that the questions are properly formatted
# then create a question object with the question and correct answer 
# use list comprehension to do that for all the questions in question_data
question_bank = [Question(unescape(question['question']), question['correct_answer']) for question in question_data] 

# create our quiz logic
quiz = QuizBrain(question_bank)
# create our quiz interface
quiz_ui = QuizInterface(quiz)

# start it by triggering the next question
quiz_ui.get_next_question()

