from pywebio.input import input as input_pw
from pywebio.output import put_text

formatted_name = put_text(f'Ура, Літо')
formatted_name = input_pw(f'Ура, Літо')

put_text('''Жив собі в лісі зайчисько малий,
    Сонце
    йому
    світило, і
    світ
    був
    такий.
    Стрибав
    він
    у
    траві, як
    радісний
    спів,
    Та
    завжди
    посміхався, хоч
    світ
    був
    суворий. 😊🌿
    ''')

plans = input_pw('Введіть ваші плани на літо:')

put_text(f'Кількість символів у ваших планах на літо:')