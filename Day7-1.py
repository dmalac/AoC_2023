import collections

# class Hand is a structure containing the card combination, the point value and the type of each hand
class Hand:
	def __init__(self, line):
		self.cards = list(line.split()[0])
		self.points = int(line.split()[1])
		self.label = self.getLabel()

	# assigns the appropriate type for each hand
	def getLabel(self):
		cardCounter = collections.Counter(self.cards)
		if max(cardCounter.values()) == 5:
			return "5oK"
		elif max(cardCounter.values()) == 4:
			return "4oK"
		elif max(cardCounter.values()) == 3:
			if min(cardCounter.values()) == 2:
				return "FH"
			else:
				return "3oK"
		elif list(cardCounter.values()).count(2) == 2:
			return "2P"
		elif list(cardCounter.values()).count(2) == 1:
			return "1P"
		else:
			return "HC"

	# compares a hand to another hand
	def isSmaller(self, hand) -> bool:
		for i, ch in enumerate(hand.cards):
			if cardStrength.index(self.cards[i]) > cardStrength.index(ch):
				return True
			elif cardStrength.index(self.cards[i]) < cardStrength.index(ch):
				return False
		return False


# returns the position in the list where a hand belongs
# assumes that the list should be sorted from lowest to highest
def whereDoesItFit(hand: Hand, lst: list) -> int:
	for i, item in enumerate(lst):
		if hand.isSmaller(item):
			return i
	return len(lst)


hands = {}
labels = ["HC", "1P", "2P", "3oK", "FH", "4oK", "5oK"]
cardStrength = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]

with open("input.txt") as f:
	for line in f.readlines():
		hand = Hand(line)
		if hand.label not in hands:
			hands[hand.label] = [hand]
		else:
			idx = whereDoesItFit(hand, hands[hand.label])
			hands[hand.label].insert(idx, hand)

result1 = []
pt = 1
# iterates over the sorted hands in the dictionary (variable "hands") from lowest to highest value
# and calculates the number of points for each one
for l in labels:
	if l in hands:
		for item in hands[l]:
			result1.append(item.points * pt)
			pt += 1

print("Result 1:", sum(result1))
