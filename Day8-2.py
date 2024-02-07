import re, math

instructions = []
nodes = {}
youAreHere = []

with open("input.txt") as f:
	instructions, rest = f.read().split('\n\n')
	for line in rest.split('\n'):
		if line:
			tmp = re.findall(r"\w+", line)
			nodes.update({tmp[0]: (tmp[1], tmp[2])})
			if tmp[0][-1] == 'A':
				youAreHere.append(tmp[0])

moves = 0
logs = [[] for i in range(6)]

# loop to identify the frequencies with which each of the six ghosts appears at a location ending with 'Z'
while any(len(x) < 1 for x in logs):
	for i in instructions:
		moves += 1
		for p, place in enumerate(youAreHere):
			youAreHere[p] = nodes[place][0] if i == 'L' else nodes[place][1]
			if youAreHere[p][-1] == 'Z':
				logs[p].append(moves)

print("Result 2: ", math.lcm(*[l[0] for l in logs]))
