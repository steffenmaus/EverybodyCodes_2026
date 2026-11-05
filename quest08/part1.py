with open('input1.txt') as file:
    lines = [line.rstrip() for line in file]


def f(starts, dx, dy):
    affected = set()
    for s in starts:
        height = 0
        x, y = s
        while (x, y) in maze and maze[(x, y)] != '.':
            if maze[(x, y)] >= height:
                affected.add((x, y))
            height = max(height - 1, maze[(x, y)])
            x += dx
            y += dy

    return affected


X = len(lines[0])
Y = len(lines)

maze = {}
for y in range(Y):
    for x in range(X):
        c = lines[y][x]
        if c != '.':
            c = int(c)
        maze[(x, y)] = c

starts_top = set([(x, 0) for x in range(X) if maze[(x, 0)] != '.'])

starts_top_left = set()
x, y = min(starts_top)
while (x, y) in maze:
    starts_top_left.add((x, y))
    x -= 1
    y += 1

print(len(f(starts_top_left | starts_top, 1, 1)))
