class Question:
    def __init__(self, question, difficulty, right_answer):
        self.question = question
        self.difficulty = difficulty
        self.right_answer = right_answer

        self. is_asked = False
        self.user_answer = None
        self.score = difficulty * 10

    def get_points(self):
        return self.score

    def is_correct(self):
        return self.user_answer == self.right_answer

    def build_question(self):
        return f'{self.question} \nСложность {self.difficulty}'

    def build_feedback(self):
        if self.is_correct():
            return f'Ответ верный, получено {self.score} баллов'
        return f'Ответ неверный, верный ответ {self.right_answer}'

