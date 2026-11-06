with open('input1.txt') as file:
    lines = [line.rstrip() for line in file]

total = 0

for l in lines:
    a, b, c = l.split(",")
    id = a.split("=")[1]
    growth = int(b.split("=")[1])
    limit = int(c.split("=")[1])

    branches = [0]
    points = 0
    time = 0
    while sum(branches) + points < limit:
        next_branches = []
        for b in branches:
            if b == growth - 1:
                next_branches.append(growth // 2)
                next_branches.append(growth // 2)
                next_branches.append(1)
                points += 1
            else:
                next_branches.append(b + 1)
        branches = next_branches
        time += 1

    total += max(time, 1)

print(total)
