from pywebio import start_server
from pywebio.input import input, select, textarea, slider, radio
from pywebio.output import put_text, put_success, put_warning
from pywebio.session import hold, run_js
import time

reviews_info = []

def main():
    user_name = input("Введіть ваше ім'я:", type="text")
    movie_name = input("Введіть назву фільму:", type="text")
    movie_genre = select("Виберіть жанр фільму:", ['Драма', 'Комедія', 'Бойовик', 'Фантастика', 'Мультфільм'])
    movie_review = textarea("Введіть короткий відгук про фільм:", rows=3, placeholder="Ваш відгук...")
    movie_rating = slider("Встановіть рейтинг фільму (від 1 до 10):", min_value=1, max_value=10, value=5)
    movie_emotions = select("Виберіть ваші емоції після перегляду фільму:", ['Щасливий', 'Сумний', 'Захоплений', 'Розчарований'])
    movie_recommend = radio("Чи рекомендуєте ви цей фільм іншим?", options=['Так', 'Ні'])


    review = {
        'name': user_name,
        'movie': movie_name,
        'rating': movie_rating,
        'recommend': movie_recommend
    }
    reviews_info.append(review)


    if movie_rating >= 8:
        put_success('Дякуємо за високий рейтинг!')
    else:
        put_warning('Дякуємо за ваш відгук!')

    put_text(f'Ваш відгук було додано: ')

    time.sleep(4)
    run_js('window.location.reload()')

if __name__ == '__main__':
    start_server(main, port=8080)
