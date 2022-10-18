krotka = "Tomek", "Damian", "Mariusz", 55, 44.5
dane = (43, 43, 55, 666, 3312, 423, 7667, 343, 786, 437, 34, 65, 3)
print(krotka[-1])
for i in krotka:
    print(i)

numbers = [10, 34] * 2
print(numbers)
number2 = tuple(numbers)
numbers.clear()
print(number2)
number3 = list(number2)
print(number3, "Tomek")

