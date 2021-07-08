from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for item in question_data:
    q_text = item["text"]
    q_answer = item["answer"]
    question = Question(q_text, q_answer)
    question_bank.append(question)

quiz_brain = QuizBrain(question_bank)
while quiz_brain.still_has_questions():
    quiz_brain.next_question()
print("You've completed the quiz!")
print(f"Your final score was: {quiz_brain.score}/{len(quiz_brain.question_list)}")
