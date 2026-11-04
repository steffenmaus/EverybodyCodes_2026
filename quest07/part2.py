from collections import defaultdict

with open('input2.txt') as file:
    lines = [line.rstrip() for line in file]

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

open = defaultdict(lambda: defaultdict(int))
open[start][10] = 1
while open:
    next = defaultdict(lambda: defaultdict(int))
    for id in energies:
        for imp, count in open[id].items():
            energies[id] += imp * count
            if imp > 1:
                for c in connections[id]:
                    next[c][imp - 1] += count
    open = next

print(sum(energies.values()))
