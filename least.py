
values = []

num = input()
num = int(num)
n = input()
n = int(n)
x = 0
i = 0
tempVar = ""
while (num >0):
    tempVar = num%10;
    values.append(tempVar)
    num = num/10
values.sort()
n = len(values) - n;
while (n>0):
    x = x*10 + values[i]
    n = n-1
    i = i+1  
print x    