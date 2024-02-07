def nextNumber(seq: list) -> list:
	if all(x == 0 for x in seq):
		return [0, 0]
	newSeq = [seq[i] - seq[i-1] for i in range(1, len(seq))]
	prev, next = nextNumber(newSeq)
	return [seq[0] - prev, seq[-1] + next]


result1 = []
result2 = []

with open("input.txt") as f:
	for line in f.readlines():
		nums = (nextNumber([int(x) for x in line.split()]))
		result1.append(nums[1])
		result2.append(nums[0])

print("Result 1:", sum(result1))
print("Result 2:", sum(result2))
