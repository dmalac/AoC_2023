import re

instructions = []
nodes = {}

with open("input.txt") as f:
	instructions, rest = f.read().split('\n\n')
	for line in rest.split('\n'):
		if line:
			tmp = re.findall(r"\w+", line)
			nodes.update({tmp[0]: (tmp[1], tmp[2])})

youAreHere = 'AAA'
moves = 0
while youAreHere != 'ZZZ':
	for i in instructions:
		youAreHere = nodes[youAreHere][0] if i == 'L' else nodes[youAreHere][1]
		moves += 1

print("Result 1:", moves)