
forLater = []
up = (-1, 0)
down = (1, 0)
left = (0, -1)
right = (0, 1)

def addCoord(a: tuple, b: tuple) -> tuple:
	return tuple(sum(x) for x in list(zip(a, b)))

def calculateNextStep(pos: tuple, dir: tuple, tile: chr) -> dict:
	if tile == '.' or (tile == '-' and dir[0] == 0) or (tile == '|' and dir[1] == 0):
		return {addCoord(pos, dir): dir}
	elif tile == '|':
		return {addCoord(pos, up): up, addCoord(pos, down): down}
	elif tile == '-':
		return {addCoord(pos, left): left, addCoord(pos, right): right}
	elif tile == '/':
		return {addCoord(pos, (-dir[1], -dir[0])): (-dir[1], -dir[0])}
	else:
		return {addCoord(pos, (dir[1], dir[0])): (dir[1], dir[0])}

def isInsideGrid(y: int, x: int) -> bool:
	if 0 <= y < len(grid) and 0 <= x < len(grid[0]):
		return True
	return False

def sendBeam(grid: list, q: list, tiles: dict) -> int:
	while q:
		# find tiles to which we move from the current position
		nextTiles = calculateNextStep(q[0], tiles[q[0]][-1], grid[q[0][0]][q[0][1]])
		for key, val in nextTiles.items():
			if isInsideGrid(*key):
				# if the beam splits, only the first subbeam is put in the queue
				if key not in tiles and len(q) == 1:
					tiles[key] = [val]
					q.append(key)
				elif key in tiles and val not in tiles[key] and len(q) == 1:
					tiles[key].append(val)
					q.append(key)
				# the second subbeam is saved to be processed later
				elif key not in tiles or (key in tiles and val not in tiles[key]):
					forLater.append({key: val})
		q.pop(0)
		# once the queue is empty, subbeams saved for later processing are dealt with
		if not q and forLater:
			for k, v in forLater[0].items():
				if k not in tiles:
					tiles[k] = [v]
				elif v not in tiles[k]:
					tiles[k].append(v)
				q.append(k)
				forLater.pop(0)
	return(len(tiles))

with open("input.txt") as f:
	grid = [x for x in [line.strip() for line in f.readlines()]]
	result1 = sendBeam(grid, [(0, 0)], {(0, 0): [right]})
	print("Result 1:", result1)
	result2 = []
	for y in range(len(grid)):
		for x in range(len(grid[0])):
			if y == 0:
				result2.append(sendBeam(grid, [(y, x)], {(y, x): [down]}))
			if x == 0:
				result2.append(sendBeam(grid, [(y, x)], {(y, x): [right]}))
			if y == len(grid) - 1:
				result2.append(sendBeam(grid, [(y, x)], {(y, x): [up]}))
			if x == len(grid[0]):
				result2.append(sendBeam(grid, [(y, x)], {(y, x): [left]}))
	print("Result 2:", max(result2))
