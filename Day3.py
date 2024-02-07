import re

batch = [[]]
result1, result2 = [0, 0]
potentialGears = {}


def scanSurroundings(batch: list, left: int, right: int, topLineNr: int, number: int):
	start = max(left, 0)
	end = min(right, len(batch[1]) - 1)
	isAdjacent = False
	global result1
	for l, line in enumerate(batch):
		if line:
			for i in range(start, end + 1):
				# PART 1
				if not isAdjacent and not (line[i] == '.' or line[i].isdigit()):
					isAdjacent = True
					result1 += number
				# PART 2
				if line[i] == '*':
					if (topLineNr + l, i) in potentialGears:
						potentialGears[(topLineNr + l, i)] += [number]
					else:
						potentialGears[(topLineNr + l, i)] = [number]


with open("input.txt") as f:
	batch.extend(f.readline().strip() for i in range(2))
	topLineNr = -1
	while batch[1]:
		matches = re.finditer(r'\d+', batch[1])
		for m in matches:
			scanSurroundings(batch, m.start() - 1, m.end(), topLineNr, int(m.group(0)))
		batch.append(f.readline().strip())
		batch = batch[1:]
		topLineNr += 1

# PART 1
print("Result 1: ", result1)

# PART 2
for key, val in potentialGears.items():
	if len(val) == 2:
		result2 += val[0] * val[1]
print("Result 2: ", result2)
