import re, math
from collections import deque

idx = {'x': 0, 'm': 1, 'a': 2, 's': 3}

def process(xmas: tuple, label: str) -> int:
	while label:
		for cond in wf[label]:
			if len(cond) == 1:
				if cond[0] == 'A':
					return sum(xmas)
				elif cond[0] == 'R':
					return 0
				else:
					label = cond[0]
					break
			if cond[1] == '<':
				if xmas[idx[cond[0]]] < cond[2]:
					if cond[3] == 'A':
						return sum(xmas)
					elif cond[3] == 'R':
						return 0
					label = cond[3]
					break
			else:
				if xmas[idx[cond[0]]] > cond[2]:
					if cond[3] == 'A':
						return sum(xmas)
					elif cond[3] == 'R':
						return 0
					label = cond[3]
					break

def splitConfig(pos: int, sign: chr, val: int, config: list) -> list:
	through, rest = [[], []]
	for i in range(len(idx)):
		if i == pos and sign == '<':
			through.append([config[i][0], min(config[i][1], val - 1)] if config[i][0] < val else 0)
			rest.append([val, config[i][1] if config[i][1] >= val else 0])
		elif i == pos:
			through.append([val + 1, config[i][1]] if config[i][1] > val else [0, 0])
			rest.append([config[i][0], val] if config[i][0] <= val else [0, 0])
		else:
			through.append(config[i])
			rest.append(config[i])
	return through, rest

def calculateAccepted(wf: dict, ) -> int:
	q = deque([('in', [[1, 4000], [1, 4000], [1, 4000], [1, 4000]])])
	acc = []
	accepted = 0
	rej = []
	rejected = 0
	while q:
		current = q.popleft()
		label = current[0]
		config = current[1]
		for cond in wf[label]:
			if len(cond) == 1:
				if cond[0] == 'A':
					accepted += math.prod([x[1] - x[0] + 1 for x in config])
					acc.append(config)
				elif cond[0] == 'R':
					rejected += math.prod([x[1] - x[0] + 1 for x in config])
					rej.append(config)
				else:
					q.append((cond[0], config))
					break
			else:
				through, config = splitConfig(idx[cond[0]], cond[1], cond[2], config)
				if 0 not in through[idx[cond[0]]]:
					if cond[3] == 'A':
						accepted += math.prod([x[1] - x[0] + 1 for x in through])
						acc.append(through)
					elif cond[3] == 'R':
						rejected += math.prod([x[1] - x[0] + 1 for x in through])
						rej.append(through)
					else:
						q.append((cond[3], through))
				if 0 in config[idx[cond[0]]]:
					break
	return accepted

wf = {}
result1 = []

with open("input.txt") as f:
	tmpwf, parts = f.read().split('\n\n')
	# Workflows
	for line in tmpwf.split('\n'):
		label, cond, _ = re.split("[{}]", line)
		cond = cond.split(',')
		wf[label] = []
		for c in cond:
			tmpCond = re.findall("[a-zA-Z]+|[<>]|\d+", c)
			if len(tmpCond) > 1:
				tmpCond[2] = int(tmpCond[2])
			wf[label].append(tmpCond)
	# Parts
	for line in parts.split('\n'):
		xmas = tuple([int(x) for x in re.findall("\d+", line)])
		result1.append(process(xmas, "in"))

print("Result 1:", sum(result1))
print("Result 2:", calculateAccepted(wf))
