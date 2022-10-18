# for hours in range(24):
#     for minutes in range(60):
#         for seconds in range(60):
#             print(hours, minutes, seconds, sep=":")

rows = 5
cols = 10

# for r in range(rows):
#     for c in range(cols):
#         print('*', end='^')
#     print()

for r in range(rows):
    for c in range(r + 1):
        print('*', end='')
    print("o")