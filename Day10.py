steps = [(-1, 0), (1, 0), (0, -1), (0, 1)]

pipes = {'|': [(-1, 0), (1, 0)],
		 '-': [(0, -1), (0, 1)],
		 'L': [(-1, 0), (0, 1)],
		 'J': [(-1, 0), (0, -1)],
		 '7': [(0, -1), (1, 0)],
		 'F': [(0, 1), (1, 0)]}

# returns coordinates of the 'S' character
def findStart() -> tuple:
	for i, m in enumerate(maize):
		if 'S' in m:
			return (i, m.index('S'))

# checks whether coordinates are outside the map
def isOutsideMap(y: int, x: int) -> bool:
	if 0 <= y < len(maize) and 0 <= x < len(maize[0]):
		return False
	else:
		return True

# checks whether a pipe piece is connected to the current position
# (using the description of the step necessary to reach the assessed piece)
def isConnected(step: tuple, pipe: chr) -> bool:
	if pipe in pipes:
		for move in pipes[pipe]:
			if step == tuple([-1 * x for x in move]):
				return True
	return False

# adds two coordinates
def addCoord(a: tuple, b: tuple) -> tuple:
	return tuple([sum(x) for x in zip(a, b)])

# returns the coordinates of the field to which one moves from the starting position
def firstStep(pos: tuple) -> tuple:
	for s in steps:
		y, x = addCoord(pos, s)
		if isOutsideMap(y, x):
			continue
		if isConnected(s, maize[y][x]):
			return addCoord(pos, s)

# returns the coordinates of the next visited field
def nextStep(pos: tuple, pipe: chr, pipeLoop: list) -> tuple:
	for move in pipes[pipe]:
		nxt = addCoord(pos, move)
		if nxt not in pipeLoop:
			return nxt
	return -1, -1

def solvePart1(pos: tuple):
	global pipeLoop
	pipeLoop.append(pos)
	pos = firstStep(pos)
	while pos != (-1, -1):
		pipeLoop.append(pos)
		pos = nextStep(pos, maize[pos[0]][pos[1]], pipeLoop)
	print("Result 1:", int(len(pipeLoop) / 2))

# locates the next corner of the pipe loop and returns its type and index
def findNextCorner(y: int, x: int) -> [chr, int]:
	if 'J' not in maize[y][x + 1:]:
		return '7', maize[y].index('7', x + 1)
	elif '7' not in maize[y][x + 1:]:
		return 'J', maize[y].index('J', x + 1)
	else:
		if maize[y].index('J', x + 1) < maize[y].index('7', x + 1):
			return 'J', maize[y].index('J', x + 1)
		else:
			return '7', maize[y].index('7', x + 1)

# returns (i) the index of the first following field that is not part of the pipe loop
# and (ii) whether the pipe has been crossed (inside to outside or outside to inside) (variable c)
def skipPipe(y: int, x: int, c: int) -> [int, chr]:
	char = maize[y][x]
	if char == '|':
		return x + 1, c + 1
	elif char == 'L' or char == 'F':
		nextCorner, x = findNextCorner(y, x)
		if (char + nextCorner) in ['LJ', 'F7']:
			return x + 1, c
		else:
			return x + 1, c + 1

# identifies which pipe shape belongs in the starting position
def replaceS():
	global maize
	y, x = findStart()
	movesFromS = [(pipeLoop[1][0] - pipeLoop[0][0], pipeLoop[1][1] - pipeLoop[0][1]),
				  (pipeLoop[-1][0] - pipeLoop[0][0], pipeLoop[-1][1] - pipeLoop[0][1])]
	for key, value in pipes.items():
		if len(set(value) & set(movesFromS)) == 2:
			maize[y][x] = key

def solvePart2():
	global maize
	replaceS()
	y, c = [0, 0]
	newChar = ['O', 'I']
	while y < len(maize):
		x = 0
		while x < len(maize[0]):
			if (y, x) in pipeLoop:
				x, c = skipPipe(y, x, c)
			else:
				maize[y][x] = newChar[c % 2]
				x += 1
		y += 1
	result2 = 0
	for m in maize:
		result2 += m.count('I')
	print("Result 2: ", result2)

with open("input.txt") as f:
	maize = [list(x) for x in f.read().split('\n')]
	pipeLoop = []
	pos = findStart()
	solvePart1(pos)
	solvePart2()
