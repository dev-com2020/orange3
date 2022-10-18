def dodawanie():
    suma = 2 + 2
    print(suma)


def odejmowanie(a, b):
    suma = a - b
    print(suma)


def mnozenie(a=1, b=1):
    suma = a * b
    print(suma)


print("Tutaj program sobie działa...")
print("Menu: wybierz 1 żeby dodać liczby lub 2 żeby odjąć, lub 3 żeby pomnożyć!")
wybor = input("Podaj swój wybór")
if wybor == "1":
    dodawanie()
elif wybor == "2":
    odejmowanie(5, 2)
elif wybor == "3":
    mnozenie()
