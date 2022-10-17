name = input('Jak masz na imię? ')
age = int(input('Ile masz lat? '))
if age < 18:
    print(f'Cześć {name},jesteś zbyt młody!')
elif age == 18:
    print(f'Cześć {name},masz 18 lat!!')
else:
    print('Masz więcej niż 18 lat...')

    # print("Jestem w środku ifa...")
# print("Jestem poza ifem...")

podaj = input("Podaj hasło!:")
haslo = "12345"
if haslo == podaj:
    print("Wszedłeś!")


'''
if warunek:
    polecenie
    
'''