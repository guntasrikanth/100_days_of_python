from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
print("Welcome to the Quiz Game. Hope you had great day.")
for i in question_data:
    question_text = i["question"]
    answer = i["correct_answer"]
    question_object = Question(question_text, answer)
    question_bank.append(question_object)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz.")
print(f"You final score is: {quiz.score}/{quiz.question_number}.")
