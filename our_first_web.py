from pywebio.input import input as input_pw
from pywebio.input import NUMBER
from pywebio.output import put_text, put_html, put_image

def main():

    put_html('<h1>УРА, ЛІТО!</h1>')

    put_html(f'''<h2>Жив собі в лісі зайчисько малий,  
    Сонце йому світило, і світ був такий.  
    Стрибав він у траві, як радісний спів,  
    Та завжди посміхався, хоч світ був суворий. 😊🌿 </h2> 
    ''')

    plans = input("Введіть ваші плани на літо:", type=TEXT)


    char_count = len(plans)
    put_text(f'Кількість символів у ваших планах: {char_count}')

    img = open('images.jpg', 'rb').read()
    put_image(img, width='500px')


