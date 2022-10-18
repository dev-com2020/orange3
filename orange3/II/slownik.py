slownik = {1: "Tomek",
           2: "Jarek",
           "imie": "Aga",
           "rok": 1988
           }

print(slownik[1])
slownik["rok"] = 2022
slownik["godzina"] = 11
slownik["tabela"] = [5, 3, 4, 6, 3, 66]
print(slownik["imie"])
print(slownik["rok"])
print(slownik.items())
print(slownik.keys())
print(slownik.values())

# if "rok" in slownik:
#     print(slownik["rok"])
# if "rok2" not in slownik:
#     print("Nie znaleziono klucza o wartości rok2")

szukam_Tomka = [klucz for klucz, wartosc in slownik.items() if wartosc == "Tomek"]
print(szukam_Tomka, "🥳")

lista = [i for i in range(5)]
print(lista)

liczby = ["1", 2, '4', '5']
liczby2 = [int(i) for i in liczby]
print(liczby2)

slownik2 = {1: "Tomek", 2: "Jarek", 3: "Aga"}
print({wartosc: klucz for klucz, wartosc in slownik2.items()})
