from math import prod

result1 = []
result2 = []

def calculateWins(t: list, d: list) -> list:
	total = [0 for i in range(len(t))]
	for idx, item in enumerate(t):
		for s in range(1, item):
			if (item - s) * s > d[idx]:
				total[idx] += 1
	return total

with open("input.txt") as f:
	lines, distances = f.readlines()
	# PART 1
	times1 = [int(x) for x in lines.split(':')[1].strip().split()]
	distances1 = [int(x) for x in distances.split(':')[1].strip().split()]
	result1 = calculateWins(times1, distances1)

	# PART 2
	time2 = [int("".join(lines.split(':')[1].strip().split()))]
	distance2 = [int("".join(distances.split(':')[1].strip().split()))]
	result2 = calculateWins(time2, distance2)

print("Result 1: ", prod(result1))
print("Result 2: ", result2[0])
