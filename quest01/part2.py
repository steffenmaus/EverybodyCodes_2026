import math

with open('input2.txt') as file:
    lines = [line.rstrip() for line in file]


def f(n):
    if n < 8:
        return 8
    r = n / 4
    if r == int(r):
        return n
    else:
        return math.ceil(r) * 4


total = 0
for n in lines[0].split(","):
    n = int(n)
    m = f(n)
    total += m - n

print(total)
