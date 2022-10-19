lista1 = [1, 2, 3, 4]
lista2 = [2, 3, 4, 5]
wynik = []
idx = 0
for i in lista1:
    wynik.append(i + lista2[idx])
    idx += 1
print(wynik)

Lista1 = [1, 2, 3, 4]
Lista2 = [2, 3, 4, 5]
Lista3 = []
for i in range(4):
    Lista3.append(Lista1[i]+Lista2[i])
print(Lista3)
