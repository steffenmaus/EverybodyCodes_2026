from collections import defaultdict

with open('input1.txt') as file:
    lines = [line.rstrip() for line in file]

items = defaultdict(list)

for l in lines:
    item, ing = l.split(":")
    items[item] = ing.split(",")

sol = set()


def f(item):
    for i in items[item]:
        if i not in sol and i != "NULL":
            sol.add(i)
            f(i)


f("NULL")

print(len(sol))
