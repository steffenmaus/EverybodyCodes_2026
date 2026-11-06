from collections import defaultdict

with open('input3.txt') as file:
    lines = [line.rstrip() for line in file]

total = 0

for l in lines:
    a, b, c = l.split(",")
    id = a.split("=")[1]
    growth = int(b.split("=")[1])
    limit = int(c.split("=")[1])

    branches = defaultdict(int)
    branches[0] = 1
    points = 0
    time = 0
    while (points + 1) < limit:
        skippable = growth - max(branches.keys()) - 1
        if skippable > 0:
            time += skippable
            next_branches = defaultdict(int)
            for branch_l, branch_c in branches.items():
                next_branches[branch_l + skippable] = branch_c
            branches = next_branches

        next_branches = defaultdict(int)
        for branch_l, branch_c in branches.items():
            if branch_l == growth - 1:
                next_branches[growth // 2] += 2 * branch_c
                next_branches[1] += branch_c
                points += branch_c
            else:
                next_branches[branch_l + 1] += branch_c
        branches = next_branches
        time += 1
    total += max(time, 1)

print(total)
