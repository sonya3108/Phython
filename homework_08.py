from pywebio import start_server
from pywebio.input import input, input_group,  TEXT, NUMBER, DATE
from pywebio.output import put_text, put_image, put_html


def main():
    total_score = 0

    name = input("Введіть ваше ім'я:", )

    questions = [
        {
            'question': 'Коли вибухнула ЧАЕС?',
            'type': NUMBER,
            'answer': 1986
        },
        {
            'question': 'Яка столиця Східної Римської імперії?',
            'type': TEXT,
            'answer': 'константинополь'
        },
        {
            'question': 'Скільки континентів на Землі?',
            'type': NUMBER,
            'answer': 7
        },
        {
            'question': 'Якого року США проголосили незалежність?',
            'type': NUMBER,
            'answer': 1776
        }
    ]

    for q in questions:
        user_answer = input(q['question'], type=q['type'])
        if q['type'] == TEXT and user_answer.lower() == q['answer']:
            total_score += 1
        elif q['type'] == NUMBER and user_answer == q['answer']:
            total_score += 1

    put_text(f'{name}, ваш результат: {total_score} з 5')

    if total_score == 5:
        put_image('five_stars.jpeg')


if __name__ == '__main__':
    start_server(main, port=8080)
