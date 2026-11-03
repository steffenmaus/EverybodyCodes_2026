import math

with open('input3.txt') as file:
    lines = [line.rstrip() for line in file]


def f(n):
    r = math.sqrt(n + 1)
    if r == int(r) and ((n + 1) % 2 == 1):
        return n
    else:
        m = math.ceil(r)
        if m % 2 == 0:
            m += 1
        return (m ** 2) - 1


total = 0
for n in lines[0].split(","):
    n = int(n)
    m = f(n)
    total += m - n

print(total)
