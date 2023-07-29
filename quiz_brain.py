import html

class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        # Remove HTML entities from the question
        cleaned_question = html.unescape(current_question.question)
        return f"Q{self.question_number}: {cleaned_question} (True/False)?: "

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong meathead")
        print(f"The answer is: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        # add a new line
        print("\n")
