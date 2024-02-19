
dirs = {'>': (0, 1), '<': (0, -1), '^': (-1, 0), 'v': (1, 0)}

def addCoord(a: tuple, b: tuple) -> tuple:
	return tuple(sum(x) for x in list(zip(a, b)))

def isInGrid(y: int, x: int) -> bool:
	if 0 <= y < len(grid) and 0 <= x < len(grid[0]):
		return True
	return False

def getPossibleSteps(grid: list, pos: tuple, visited: list) -> list:
	visited.append(pos)
	if grid[pos[0]][pos[1]] in dirs:
		nxtPos = addCoord(pos, dirs[grid[pos[0]][pos[1]]])
		return [nxtPos] if nxtPos not in visited else []
	steps = []
	for d in dirs.values():
		potPos = addCoord(pos, d)
		if isInGrid(*potPos) and potPos not in visited and grid[potPos[0]][potPos[1]] != '#':
			steps.append(potPos)
	return steps

def findWay(grid: list, pos: tuple, end: tuple, visited: list) -> list:
	res = []
	steps = getPossibleSteps(grid, pos, visited)
	while len(steps) == 1:
		pos = steps[0]
		if pos == end:
			return [len(visited) - 1]
		steps = getPossibleSteps(grid, pos, visited)
	for item in steps:
		res.extend(findWay(grid, item, end, [x for x in visited]))
	return res

with open("input.txt") as f:
	grid = [line.strip() for line in f.readlines()]
	result1 = findWay(grid, (0, grid[0].index('.')), (len(grid) - 1, grid[len(grid) - 1].index('.')), [(0, grid[0].index('.'))])
	print("Result 1:", max(result1))