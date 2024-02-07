from math import prod

bag = {'red': 12, 'green': 13, 'blue': 14}

# for PART 1
def isRoundPossible(bag, game) -> bool:
	for key, value in game.items():
		if value > bag[key]:
			return False
	return True

# for PART 2
def updateMinGameConfig(minGameConfig, game):
	for key, value in game.items():
		minGameConfig[key] = value if value > minGameConfig[key] else minGameConfig[key]

with open("input.txt") as f:
	result1 = []
	result2 = []
	for line in f.readlines():
		isGamePossible = True
		minGameConfig = {'red': 0, 'green': 0, 'blue': 0}
		id = int(line.strip().split(":")[0].split(' ')[-1])
		rounds = line.strip().split(":")[1].strip().split(";")
		for round in rounds:
			game = {}
			sets = [str.split() for str in round.split(",")]
			for value, key in sets:
				if key in game:
					game[key] += int(value)
				else:
					game[key] = int(value)
			# PART 1
			isGamePossible = isGamePossible and isRoundPossible(bag, game)
			# PART 2
			updateMinGameConfig(minGameConfig, game)
		if isGamePossible:
			result1.append(id)
		result2.append(prod(minGameConfig.values()))
	print("Result PART 1: ", sum(result1))
	print("Result PART 2: ", sum(result2))

