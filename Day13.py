
def isAlmostSame(a, b) -> bool:
	return True if sum([1 if x[0] != x[1] else 0 for x in list(zip(a,b))]) == 1 else False

def findMatchesOfTopAndBottomRow(p: list, matches1: list, matches2: list):
	for l, line in enumerate(p):
		if l != 0 and l % 2 == 1:
			if line == p[0] and (0, l) not in matches1:
				matches1.append((0, l))
			if (line == p[0] or isAlmostSame(line, p[0])) and (0, l) not in matches2:
				matches2.append((0, l))
		if l != len(p) - 1 and (len(p) - 1 - l) % 2 == 1:
			if line == p[len(p) - 1] and (l, len(p) - 1) not in matches1:
				matches1.append((l, len(p) - 1))
			if (line == p[len(p) - 1] or isAlmostSame(line, p[len(p) - 1])) and (l, len(p) - 1) not in matches2:
				matches2.append((l, len(p) - 1))

def whereIsMirror(p: list, top: int, bottom: int, same: bool, almostSame: bool) -> int:
	while same and bottom > top:
		if p[top] != p[bottom]:
			if almostSame and isAlmostSame(p[top], p[bottom]):
				almostSame = False
			else:
				same = False
		top += 1
		bottom -= 1
	return top if same and not almostSame else -1


def findMirror(p: list) -> list:
	matches1 = []
	matches2 = []
	findMatchesOfTopAndBottomRow(p, matches1, matches2)
	res1, res2 = [[0], [0]]
	for m in matches1:
		mirrorPosition = whereIsMirror(p, *m, True, False)
		if mirrorPosition > 0:
			res1.append(mirrorPosition)
	for m in matches2:
		mirrorPosition = whereIsMirror(p, *m, True, True)
		if mirrorPosition > 0:
			res2.append(mirrorPosition)
	return max(res1), max(res2)

def flipPattern(p: list) -> list:
	flipped = []
	for i in range(len(p[0])):
		flipped.append("".join([x[i] for x in p]))
	return flipped

result1 = []
result2 = []

with open("input.txt") as f:
	patterns = [x.split('\n') for x in f.read().split('\n\n')]
	for i, p in enumerate(patterns):
		res1, res2 = [0, 0]
		hor1, hor2 = [0, 0]
		fli1, fli2 = [0, 0]
		hor1, hor2 = [x  * 100 for x in findMirror(p)]
		if hor1 == 0 or hor2 == 0:
			flipped = flipPattern(p)
			fli1, fli2 = findMirror(flipped)
		result1.append(max(hor1, fli1))
		result2.append(max(hor2, fli2))
	
print("Result1: ", sum(result1))
print("Result2: ", sum(result2))