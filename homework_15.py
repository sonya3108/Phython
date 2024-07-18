import requests
import json

def download_pdf(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"PDF файл збережено як {filename}")
    else:
        print(f"Не вдалося завантажити файл. Статус код: {response.status_code}")

def fetch_and_save_data(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"Дані успішно збережені у файл {filename}")
    else:
        print(f"Не вдалося отримати дані. Статус код: {response.status_code}")


pdf_url = "https://chtyvo.org.ua/authors/Falkovych_Hryhorii/Smyk-tyndyk.pdf"

pdf_filename = "Smyk-tyndyk.pdf"

download_pdf(pdf_url, pdf_filename)

json_url = "http://api.open-notify.org/astros.json"
json_filename = "astros.json"

fetch_and_save_data(json_url, json_filename)

