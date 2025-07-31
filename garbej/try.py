import random
import json

acc = {}

try:
    with open("garbej/test.json", 'r') as file:
        acc = json.load(file)

except FileNotFoundError:
    acc = {}

ac = str(random.randint(1, 3))


if ac not in acc:
    acc[ac] = {}
    

acc[ac]["Ac. no"] = ac

print(acc)

with open("garbej/test.json", 'w') as file:
    json.dump(acc, file, indent=4)

