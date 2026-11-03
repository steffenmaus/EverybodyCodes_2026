from collections import defaultdict

with open('input2.txt') as file:
    lines = [line.rstrip() for line in file]

parents = defaultdict(list)

for l in lines:
    item, ing = l.split(":")
    for i in ing.split(","):
        parents[i].append(item)

sol = set()


def f(item):
    for p in parents[item]:
        if p not in sol and p != "NULL":
            sol.add(p)
            f(p)


f("NULL")

print(len(sol))
