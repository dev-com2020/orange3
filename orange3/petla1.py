keep_going = 't'

while keep_going == 't':
    orig_price = float(input("Podaj cenę detaliczną:"))
    rabat = orig_price * 0.2
    cena_sprz = orig_price - rabat
    print("cena finalna=", cena_sprz)
    print("-" * 20)
    keep_going = input("Czy chcesz obliczyć kolejną cenę?(Jeśli tak, wpisz 't'):")

# licznik = 0
# while True:
#     licznik += 1  # licznik = licznik + 1
#     if licznik > 10:
#         print(licznik)
#         break
#
# napis = "15"
# for litera in napis:
#     print(litera)
#
# for i in range(10):
#     print("hej, jestem w iteracji nr", i)
#     print(i + 3)
