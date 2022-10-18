lista = [4, 6, 8, 0]
lista2 = [24, 36, 58, 70]
lista3 = []

# plik = open("baza.tx3", 'w')
# plik = open("baza.tx3", 'r')
# plik = open("baza.tx3", 'a')
# plik2 = open(r'D:\test.txt', 'w')
plik3 = open('dane.txt', 'r', encoding="utf-8")

print(plik3.read())

# plik.write("\n")
# plik.write(str(lista2))

# for i in plik:
#     lista3.append(i)
#
# print(lista3)

plik3.close()
