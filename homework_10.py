from pywebio.input import textarea, select, checkbox, radio, FLOAT, DATE, PASSWORD, DATETIME, input as input_pw, slider, input_group
from pywebio.output import put_success, put_error, put_warning, put_image, put_html, put_table
from pywebio import start_server
import random


students = {
    'Іван Петров': {
        'Пошта': 'Ivan@gmail.com',
        'Вік': 14,
        'Номер телефону': '+380987771221',
        'Середній бал': 95.8
    },
    'Женя Курич': {
        'Пошта': 'Geka@gmail.com',
        'Вік': 16,
        'Номер телефону': None,
        'Середній бал': 64.5
    },
    'Маша Кера': {
        'Пошта': 'Masha@gmail.com',
        'Вік': 18,
        'Номер телефону': '+380986671221',
        'Середній бал': 80
    },
    }
new_student = {
    'Пошта': 'Pavlo@gmail.com',
    'Вік': random.randint(18, 40),
    'Номер телефону': '+380987654321',
    'Середній бал': random.uniform(0, 100)
}
students['Павло Іванов'] = new_student


print(f"Додано нового студента: Павло Іванов, Вік: {new_student['Вік']}, Середній бал: {new_student['Середній бал']:.2f}")


high_achievers = [f"{name} (Середній бал: {info['Середній бал']:.2f})" for name, info in students.items() if info['Середній бал'] > 90]


print("\nСписок студентів з середнім балом більше 90:")
for student in high_achievers:
    print(student)


average_score = sum(info['Середній бал'] for info in students.values()) / len(students)


print(f"\nСередній бал по групі: {average_score:.2f}")

for name, info in students.items():
    if not info['Номер телефону']:
        info['Номер телефону'] = '+380123456789'
        print(f"Для студента {name} додано номер телефону батьків: {info['Номер телефону']}")


