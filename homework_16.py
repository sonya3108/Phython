import csv

file_path = 'airport-codes_csv.csv'

with open(file_path, mode='r', encoding='utf-8') as file:
    reader = csv.reader(file, delimiter=';')
    header = next(reader)

    name_idx = header.index('name')
    iso_country_idx = header.index('iso_country')

    ukraine_airports_names = []

    for row in reader:
        if row[iso_country_idx] == 'UA':
            ukraine_airports_names.append(row[name_idx])

for name in ukraine_airports_names:
    print(name)



