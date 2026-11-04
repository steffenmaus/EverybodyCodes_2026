from collections import defaultdict

with open('input3.txt') as file:
    lines = [line.rstrip() for line in file]


def f(start, connections, energies):
    exploded = set()
    open = defaultdict(lambda: defaultdict(int))
    open[start][10] = 1
    while open:
        next = defaultdict(lambda: defaultdict(int))
        for id in energies.keys() ^ exploded:
            for imp, count in open[id].items():
                energies[id] += imp * count
                if imp > 1:
                    for c in connections[id]:
                        next[c][imp - 1] += count
            if energies[id] >= 1000000:
                exploded.add(id)
                for c in connections[id]:
                    next[c][10] += 1
        open = next

    return sum(energies[e] for e in energies.keys() ^ exploded)


connections = {}
energies = {}

for l in lines:
    id = l.split(",")[0].split("=")[1]
    energies[id] = int(l.split(",")[1].split("=")[1])
    c = l.split("=")[-1].split(",")
    connections[id] = c

outs = set()
for start in energies:
    outs.add(f(start, connections.copy(), energies.copy()))

print(max(outs))
