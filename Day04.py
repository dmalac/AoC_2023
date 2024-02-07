import re

result1 = 0
cards = [0 for c in range(203)]

with open("input.txt") as f:
	for line in f.readlines():
		cardNo = int(re.search("\d+", line.split(':')[0]).group(0))
		cards[cardNo] += 1
		winning = [int(x) for x in re.split(" +", line.split(':')[1].split('|')[0].strip())]
		myNums = [int(x) for x in re.split(" +", line.split(':')[1].split('|')[1].strip())]
		match = 0
		for num in myNums:
			if num in winning:
				match += 1
		# PART 1
		result1 += int(2**(match - 1))
		# PART 2
		for i in range(1, match + 1):
			cards[cardNo + i] += cards[cardNo]
print("Result 1: ", result1)
print("Result 2: ", sum(cards))
