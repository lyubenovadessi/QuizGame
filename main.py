import quiz_logo
from question_model import Question
from quiz_data import question_data
from quiz_brain import QuizBrain

print(quiz_logo.logo)

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    next_question = Question(question_text, question_answer)
    question_bank.append(next_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print(f"👏You've completed the quiz.\nYour final score is {quiz.score}/{len(question_bank)}")











