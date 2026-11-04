with open('input1.txt') as file:
    lines = [line.rstrip() for line in file]


def f(id, imp):
    energies[id] += imp
    if imp > 1:
        for c in connections[id]:
            f(c, imp - 1)


connections = {}
energies = {}
start = None
start_v = 0

for l in lines:
    id = l.split(",")[0].split("=")[1]
    energies[id] = int(l.split(",")[1].split("=")[1])
    c = l.split("=")[-1].split(",")
    connections[id] = c
    if len(c) > start_v:
        start_v = len(c)
        start = id

f(start, 5)

print(sum(energies.values()))
