import html


# Creating a question model class
class QuestionModel:

    def __init__(self, question_text, question_answer):
        self.q_text   = question_text
        self.q_answer = question_answer


class QuizBrain:

    def __init__(self, question_bank):
        self.q_bank                  = question_bank
        self.score                   =  0
        self.current_question_number =  0
        self.current_question        = None

    def still_has_question(self):
        return len(self.q_bank) > self.current_question_number

    def next_question(self):
        self.current_question = self.q_bank[self.current_question_number]
        question_text    = html.unescape(self.current_question.q_text)
        self.current_question_number += 1
        return f"{question_text}"

    def check_answer(self, user_answer):
        correct_answer = self.current_question.q_answer
        if correct_answer == user_answer:
            self.score += 1
            return True
        else:
            return False


