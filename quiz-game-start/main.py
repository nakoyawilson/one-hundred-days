from question_model import Question
from data import question_data

question_bank = []
for item in question_data:
    text = item["text"]
    answer = item["answer"]
    question = Question(text, answer)
    question_bank.append(question)
