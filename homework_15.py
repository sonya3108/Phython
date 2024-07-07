import requests
import json


pdf_url = "https://chtyvo.org.ua/authors/Falkovych_Hryhorii/Smyk-tyndyk.pdf"
pdf_response = requests.get(pdf_url)

with open("Smyk-tyndyk.pdf", "wb") as pdf_file:
    pdf_file.write(pdf_response.content)


api_url = "http://api.open-notify.org/astros.json"
api_response = requests.get(api_url)
api_data = api_response.json()


with open("astros.json", "w") as json_file:
    json.dump(api_data, json_file, indent=4)
