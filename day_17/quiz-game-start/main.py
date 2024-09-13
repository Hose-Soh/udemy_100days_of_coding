from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = [Question(q, a) for q, a in [(i["question"], i["correct_answer"]) for i in question_data]]

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your total score is: {quiz.score}/{quiz.question_number}")