# calculates how many expanded columns and rows are between two galaxies, returns the total
def expansion(a: tuple, b: tuple, m: int) -> int:
	return (len(set(range(min(x[1] for x in [a,b]), max(x[1] for x in [a,b]))) & set(extraX)) +
			len(set(range(min(x[0] for x in [a,b]), max(x[0] for x in [a,b]))) & set(extraY))) * m

# calculates the shortest path between two galaxies (= the difference between the x and y coordinates)
def shortestPath(a: tuple, b: tuple) -> int:
	path = max(x[1] for x in [a, b]) - min(x[1] for x in [a, b]) + max(x[0] for x in [a, b]) - min(x[0] for x in [a, b])
	return(path)

galaxies = []
extraX = []
extraY = []

with open("input.txt") as f:
	for y, line in enumerate(f.readlines()):
		if '#' in line:
			x = 0
			for i in range(line.count('#')):
				galaxies.append((y, line.index('#', x)))
				x = line.index('#', x) + 1
		else:
			extraY.append(y)
	for i in range(max(x[1] for x in galaxies)):
		if [x[1] for x in galaxies].count(i) == 0:
			extraX.append(i)

result1, result2 = [0, 0]

for g, glx in enumerate(galaxies):
	for i in range(g + 1, len(galaxies)):
		result1 += shortestPath(glx, galaxies[i]) + expansion(glx, galaxies[i], 1)
		result2 += shortestPath(glx, galaxies[i]) + expansion(glx, galaxies[i], 999999)

print("Result 1:", result1)
print("Result 2:", result2)
