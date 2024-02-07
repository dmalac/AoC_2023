class Map:
	def __init__(self, line):
		self.b, self.a, self.span = [int(x) for x in line.split()]

class Chunk:
	def __init__(self, nums):
		self.start, self.span = nums
		self.adjust = 0

seeds = []
locations = []
conversions = []
chunks = []


def convert(input: int, idx: int) -> int:
	for item in conversions[idx]:
		if item.a <= input < item.a + item.span:
			return input - item.a + item.b
	return input

def fallsInBracketFully(chunk: Chunk, bracket: Map) -> bool:
	return True if bracket.a <= chunk.start < bracket.a + bracket.span and \
			bracket.a <= chunk.start + chunk.span - 1 < bracket.a + bracket.span else False

def fallsInBracketBegin(chunk: Chunk, bracket: Map) -> bool:
		return True if bracket.a <= chunk.start < bracket.a + bracket.span else False

def fallsInBracketEnd(chunk: Chunk, bracket: Map) -> bool:
	return True if bracket.a <= chunk.start + chunk.span - 1 < bracket.a + bracket.span else False

def makeChunks(chunks, idx) -> list:
	i = 0
	while i < len(chunks):
		for bracket in conversions[idx]:
			# does the chunk fully fit in a bracket?
			if fallsInBracketFully(chunks[i], bracket):
				chunks[i].adjust = bracket.b - bracket.a
				break
			# does the chunk partially (only its begin) fit in a bracket, which means that we have to split it?
			elif fallsInBracketBegin(chunks[i], bracket):
				fits = bracket.span - (chunks[i].start - bracket.a)
				chunks[i].adjust = bracket.b - bracket.a
				chunks.insert(i + 1, Chunk([chunks[i].start + fits, chunks[i].span - fits]))
				chunks[i].span = fits
				i += 1
			# does the chunk partially (only its end) fit in a bracket, which means that we have to split it?
			elif fallsInBracketEnd(chunks[i], bracket):
				fits = chunks[i].start + chunks[i].span - bracket.a
				chunks.insert(i, Chunk([chunks[i].start, chunks[i].span - fits]))
				chunks[i + 1].start = bracket.a
				chunks[i + 1].span = fits
				chunks[i + 1].adjust = bracket.b - bracket.a
				i += 1
		i += 1
	# recalculating input numbers to output numbers
	for chunk in chunks:
		chunk.start += chunk.adjust
		chunk.adjust = 0
	# send chunks to the following conversion round
	if idx < len(conversions) - 1:
		chunks = makeChunks(chunks, idx + 1)
	return chunks

with open("input.txt") as f:
	parts = f.read().split('\n\n')
	tmp = [int(x) for x in parts.pop(0).split(':')[1].split()]
	seeds = [Chunk(tmp[i:i+2]) for i in range(0, len(tmp), 2)]
	for item in parts:
		conversions.append([])
		for line in item.split('\n')[1:]:
			conversions[-1].append(Map(line))
		conversions[-1].sort(key=lambda x: x.a)

# PART 1
for num in seeds:
	for c in range(len(conversions)):
		num = convert(num, c)
	locations.append(num)
print("Result 1: ", min(locations))

# PART 2
result2 = makeChunks(seeds, 0)
print("Result 2: ", min([x.start for x in result2]))
