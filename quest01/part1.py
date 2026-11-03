import math

with open('input1.txt') as file:
    lines = [line.rstrip() for line in file]


def f(n):
    r = math.sqrt(n)
    if r == int(r):
        return n
    else:
        m = math.ceil(r)
        return m ** 2


total = 0
for n in lines[0].split(","):
    n = int(n)
    m = f(n)
    total += m - n

print(total)
