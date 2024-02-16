
directions1 = {'N': {'bottom': (0, 0), 'up': (1, 0), 'next': (0, 1)}}

directions2 = {'N': {'up': (1, 0), 'next': (0, 1)},
			  'S': {'up': (-1, 0), 'next': (0, 1)},
			  'E': {'up': (0, -1), 'next': (1, 0)},
			  'W': {'up': (0, 1), 'next': (1, 0)}}

cycle = ['N', 'W', 'S', 'E']

# checks whether coordinates are within the platform
def isWithinPlatform(y: int, x: int, platform: list) -> bool:
	if 0 <= y < len(platform) and 0 <= x < len(platform[0]):
		return True
	return False

# adds two coordinates
def addCoord(a: tuple, b: tuple) -> tuple:
	return tuple([sum(x) for x in zip(a, b)])

def getBottomCoord(dir: chr, platform: list) -> tuple:
	if dir == 'N':
		return 0, 0
	if dir == 'S':
		return len(platform) - 1, 0
	if dir == 'E':
		return 0, len(platform[0]) - 1
	if dir == 'W':
		return 0, 0

def makeThemFall(bottom: tuple, up: tuple, nxt: tuple, platform: list):
	while isWithinPlatform(*bottom, platform):
		start = bottom
		pos = addCoord(bottom, up)
		while isWithinPlatform(*pos, platform):
			if platform[bottom[0]][bottom[1]] != '.':
				while isWithinPlatform(*bottom, platform) and platform[bottom[0]][bottom[1]] != '.':
					bottom = addCoord(bottom, up)
				pos = addCoord(bottom, up)
				continue
			if platform[pos[0]][pos[1]] == 'O':
				platform[bottom[0]][bottom[1]] = 'O'
				platform[pos[0]][pos[1]] = '.'
			if platform[pos[0]][pos[1]] == '#':
				bottom = pos
				continue
			pos = addCoord(pos, up)
		bottom = addCoord(start, nxt)


with open("input.txt") as f:
	platform = [list(x.strip()) for x in f.readlines()]
	makeThemFall(directions1['N']['bottom'], directions1['N']['up'], directions1['N']['next'], platform)
	result1 = 0
	for l, line in enumerate(platform):
		result1 += line.count('O') * (len(platform) - l)
	print("Result1: ", result1)
	for i in range(1, 200):
		for c in cycle:
			bottom = getBottomCoord(c, platform)
			makeThemFall(bottom, directions2[c]['up'], directions2[c]['next'], platform)
		result2 = 0
		for l, line in enumerate(platform):
			result2 += line.count('O') * (len(platform) - l)
		# Having printed out a number of results, I have observed that, after some
		# rounds, the results keep repeating and the frequency is 77. 
		# 1000000000 % 77 is 76 with the corresponding result being 86096
		print(f"{i} {i%77} ", result2)

