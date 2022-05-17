import random

from functions import load_question, build_statistics

if __name__ == '__main__':
    print('Игра начинается!')
    questions = load_question('questions.json')
    random.shuffle(questions)

    for question in questions:
        print(question.build_question())
        user_answer = input('Ответ: ')

        question.user_answer = user_answer.lower()
        question.is_asked = True

        print(question.build_feedback())

    print('Вот и всё!')
    build_statistics(questions)
