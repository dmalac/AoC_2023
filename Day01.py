import regex as re

digitsDict = {"one": "1",
				"two": "2",
				"three": "3",
				"four": "4",
				"five": "5",
				"six": "6",
				"seven": "7",
				"eight": "8",
				"nine": "9"}

# finds all digits, including digits written as words, and returns an int composed of the first and the last digit
def getDigits(line, digitsDict) -> int:
	match = re.findall(r'one|two|three|four|five|six|seven|eight|nine|[1-9]', line, overlapped=True)
	return int((match[0] if len(match[0]) == 1 else digitsDict[match[0]]) + (match[-1] if len(match[-1]) == 1 else digitsDict[match[-1]]))

with open("input.txt") as f:
	# PART 1
	input = f.readlines()
	result1 = sum([int(d[0] + d[-1]) for d in [re.findall("\d", line) for line in input]])
	print("Result 1:", result1)
	# PART 2
	result2 = 0
	for line in input:
		result2 += getDigits(line.strip(), digitsDict)
	print("Result 2:", result2)