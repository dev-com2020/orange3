import json

data = {"imie": "Tomek", "godzina": 11}
#
# with open('dane_z.json', 'w') as j:
#     json.dump(data, j, indent=4)


with open('dane.json', 'r') as j:
    dane = json.load(j)

print(dane['hobbies'][0:2])
print(dane['children'][0])




