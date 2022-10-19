import csv

# with open('addresses.csv') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=",")
#     line_count = 0
#     for row in csv_reader:
#         if line_count == 0:
#             print(f'Zawartość: {",".join(row)}')
#             line_count += 1
#         else:
#             print(f'\t{row[0]}\t{row[1]}\t{row[2]}')
#             line_count += 1
#     print(f'Wyczytano {line_count} linii.')

# with open('adres.txt', mode='r') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#     line_count = 0
#     for row in csv_reader:
#         if line_count == 0:
#             print(f'Kolumny: {", ".join(row)}')
#             line_count += 1
#         print(f'\t {row["nazwisko"]} {row["kod"]}')
#         line_count += 1
#     print(f'Wyczytano {line_count} linii.')


# with open('dane_pracownika.csv', mode='w', encoding='utf-8') as csv_file:
#     writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#     writer.writerow(['Jan Kowalski', 'IT', 'Warszawa'])
#     writer.writerow(['Janina Kowalski', 'IT', 'Warszawa'])
#     writer.writerow(['Bożena Kowalska', 'Księgowość', 'Kraków'])

with open('dane_pracownika2.csv', mode='w', encoding='utf-8') as csv_file:
    names = ['imie', 'dział', 'miejsce']
    writer = csv.DictWriter(csv_file, fieldnames=names)
    writer.writeheader()
    writer.writerow({'imie': 'Janina Kowalski', 'dział': 'IT', 'miejsce': 'Warszawa'})
    writer.writerow({'imie': 'Jan Kowalski', 'dział': 'IT', 'miejsce': 'Kielce'})

