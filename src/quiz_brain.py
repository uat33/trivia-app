class QuizBrain:
    """
    This class takes care of our quizzes logic.

    """
    def __init__(self, q_list):
        """
            Parameters: 
                q_list a list of Question objects, one for each of the questions
            
            Attributes:
                question_number: the current question's number
                questions_list: q_list
                score: the number of correct answers
                question: the question text
                correct_answer: the correct answer to the question
        
        """
        self.question_number = 0
        self.questions_list = q_list
        self.score = 0
        self.question = ""
        self.correct_answer = ""

    def next_question(self):
        """
            This method sets up the next question, while also returning that question's text.
        """
        
        # get the new question text
        question = self.questions_list[self.question_number].question
        
        # save the new question's answer in the correct_answer variable
        self.correct_answer = self.questions_list[self.question_number].answer
        

        
        self.question_number += 1 # increment the question number
        # format the question and return it
        return f"Q{self.question_number}: {question}"

    def check_answer(self, answer):

        """
            This method checks whether the user got the question correct or not.
            
            Parameters:
                answer: a boolean value representing the user's guess
        
        """
        # if the answer is equivalent to the correct answer
        if answer == self.correct_answer:
            self.score += 1 # increment the score
            return True # return true so the appropriate action can be taken in the ui
        # otherwise return false so the appropriate action can be taken in the ui
        return False
      

    def still_has_question(self):
        """
            This method checks whether there are anymore questions left in the quiz.
        """
        # return whether the current question number is less than the length of the question list
        print(self.question_number)
        return self.question_number + 1 <= len(self.questions_list) 

    
