import json

from question import Question


def load_question(filename):
    with open(filename, 'r', ) as f:
        raw_str = json.load(f)

    questions = []

    for question in raw_str:
        questions.append(
            Question(question['q'], int(question['d']), question['a'])
        )
    return questions


def build_statistics(questions):
    total_score = 0
    right_answer = 0

    for question in questions:
        if question.is_correct():
            total_score += question.score
            right_answer += 1

    print(f'Отвечено {right_answer} вопроса из {len(questions)}')
    print(f'Набрано баллов: {total_score}')
