import pandas as pd


file_path = 'airport-codes_csv.csv'


try:
    data = pd.read_csv(file_path, delimiter=';', encoding='utf-8', on_bad_lines='skip')
except UnicodeDecodeError:

    data = pd.read_csv(file_path, delimiter=';', encoding='latin1', on_bad_lines='skip')


ukraine_airports = data[data['iso_country'] == 'UA']


ukraine_airports_names = ukraine_airports['name']
print(ukraine_airports_names)



