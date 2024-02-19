import re

result1 = []
result2 = []
boxes = [{} for i in range(256)]

def hashIt(s: str) -> int:
	x = 0
	for c in s:
		x += ord(c)
		x *= 17
		x = x % 256
	return x

def removeLense(box: dict, label: str):
	if label in box:
		del box[label]

def addLense(box: dict, label: str, val: int):
	box[label] = val

with open("input.txt") as f:
	steps = f.read().split(',')
	for s in steps:
		result1.append(hashIt(s))
		label, val = re.split(r"[-=]", s)
		if '-' in s:
			removeLense(boxes[hashIt(label)], label)
		else:
			addLense(boxes[hashIt(label)], label, int(val))
print("Result 1:", sum(result1))
for b, box in enumerate(boxes):
	for i, val in enumerate(box.values()):
		result2.append((b + 1) * (i + 1) * val)
print("Result 2:", sum(result2))
