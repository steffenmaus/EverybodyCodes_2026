from collections import defaultdict

with open('input3.txt') as file:
    lines = [line.rstrip() for line in file]

parents = defaultdict(list)
NULLS = {"NULLv1", "NULLv2", "NULLv3"}

for l in lines:
    item, ing = l.split(":")
    for i in ing.split(","):
        parents[i].append(item)


def f(item):
    for p in parents[item]:
        if p not in (sol | NULLS):
            sol.add(p)
            f(p)


counts = defaultdict(int)
for n in NULLS:
    sol = set()
    f(n)
    for s in sol:
        counts[s] += 1
print(len([c for c in counts if counts[c] >= 2]))
