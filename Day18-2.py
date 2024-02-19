from shapely.geometry import Polygon

grid = []
x, y = [0, 0]
directions = {'0': (0, 1), '2': (0, -1), '3': (-1, 0), '1': (1, 0)}

def dig(dir: tuple, steps: int):
	global grid, x, y
	y += steps * dir[0]
	x += steps * dir[1]
	grid.append((y, x))

with open("input.txt") as f:
	for line in f.readlines():
		_, _, data = line.split()
		steps = int(data[2:-2], 16)
		dir = data[-2:-1]
		dig(directions[dir], int(steps))

poly = Polygon(grid).buffer(0.5, join_style="mitre")
print("Result 1:", poly.area)
