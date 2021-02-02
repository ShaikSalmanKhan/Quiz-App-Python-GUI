from data import question_data
from quiz_app import QuestionModel, QuizBrain
from ui import QuizInterface

# question bank used to store all questions & its correct answer
question_bank = []

# iterating over the question data
for item in question_data:
    question_text   = item["question"]
    question_answer = item["correct_answer"]
    question_bank.append(QuestionModel(question_text, question_answer))

# creating a quiz object
quiz = QuizBrain(question_bank)
quiz = QuizInterface(quiz)
