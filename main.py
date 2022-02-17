# Quiz Gameshow

import quiz_brain, data, question_model

question_bank = []

for i in range(0, len(data.question_data["results"])):
    question_text = data.question_data["results"][i]["question"]
    answer_text = data.question_data["results"][i]["correct_answer"]
    question_obj = question_model.Question(question_text, answer_text)
    question_bank.append(question_obj)

# for i in range(0, len(question_bank)):
#     print(question_bank[i].text)
#     print(question_bank[i].answer)

quiz = quiz_brain.QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
