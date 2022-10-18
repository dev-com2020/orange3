tytul = "Przygody z Pythonem, albo z Javą, albo z nie wiem czym!"
tytul2 = tytul.strip("m")
plik = "baza.sql"
tytul3 = tytul.replace("z Pythonem", "z Javą")
print(tytul3)
# print(tytul2)
if plik.endswith(".xls"):
    print("TO jest poprawny plik")

x = tytul.split(",")

print(x)

# cyfra = 22
# print(tytul[0:9])
# # tytul[0] = "T" # nie działa!
# print(tytul.count("o", 0))
# # print(cyfra.isdigit())
# print(tytul.upper())
# full = tytul + " " + str(cyfra)
# print(full)
#
# if "z" in tytul:
#     print("litera z jest w stringu")
