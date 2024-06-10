from pywebio.input import input as input_pw
from pywebio.output import put_text, put_html, put_image

# header
put_html(f'<h1>Ура, Літо</h1>')
put_html(f'''<h2>Жив собі в лісі зайчисько малий,  
Сонце йому світило, і світ був такий.  
Стрибав він у траві, як радісний спів,  
Та завжди посміхався, хоч світ був суворий. 😊🌿 </h2> 
''')

plans = input_pw('Введіть ваші плани на літо:')

char_count = len(plans)
put_text(f'Кількість символів у ваших планах: {char_count}')

img = open('images.jpg', 'rb').read()
put_image(img, width='500px')







