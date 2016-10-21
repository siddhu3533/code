
values = []

n = input()
n = int(n)
counterVar = 0
tempVar = 0
for counterVar in range(n):
    tempVar = input()
    values.append(tempVar)
key = 0
for key in range(n):
    if values[key] == key:
        print(key)   