class QuizBrain:

    def __init__(self, lst):
        self.question_number = 0
        self.questions_list = lst
        self.score = 0

    def next_question(self):
        current_question = self.questions_list[self.question_number]

        answer = input(f"Q.{self.question_number + 1}: {current_question.text} (True/False)?: ")
        if answer == current_question.answer:
            self.score +=1
            print(f"correct {self.score}/{len(self.questions_list)}")
        else:
            print(f"wrong {self.score}/{len(self.questions_list)}")
        self.question_number += 1

    def still_has_questions(self):
        if self.question_number < len(self.questions_list):
            return True
        return False

