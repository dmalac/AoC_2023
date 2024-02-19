from collections import deque

grid = []
x, y = [0, 0]
directions = {'R': (0, 1), 'L': (0, -1), 'U': (-1, 0), 'D': (1, 0)}

def dig(dir: tuple, steps: int):
	global grid, x, y
	for i in range(1, steps + 1):
		y += dir[0]
		x += dir[1]
		grid.append((y, x))

def fill(grid: list, pos: tuple):
	q = deque([pos])
	while q:
		current = q.popleft()
		grid.append(current)
		for d in directions.values():
			newPos = tuple(sum(x) for x in list(zip(current, d)))
			if newPos not in grid and newPos not in q:
				q.append(newPos)

def findStartForFilling(topBorder: list, grid:list) -> tuple:
	for r, c in topBorder:
		if (r + 1, c) not in grid:
			return r + 1, c

with open("input.txt") as f:
	for line in f.readlines():
		dir, steps, _ = line.split()
		dig(directions[dir], int(steps))
topBorder = [x for x in grid if x[0] == min(grid, key=lambda x: x[0])[0]]
start = findStartForFilling(topBorder, grid)
fill(grid, start)

print("Result 1:", len(grid))

