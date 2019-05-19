import random

def random_walk(n):
	x, y = 0, 0
	for i in range(n):
		(dx, dy) = random.choice([(0, 1),(0, -1),(1, 0),(-1, 0)])
		x += dx
		y += dy
	return (x, y)


number_of_walks = 10000

for walk_length in range(1, 31):
	no_transport = 0 # Number of walks 4 of fewer blocks from home
	for i in range(number_of_walks):
		(x, y) = random_walk(walk_length)
		distance = abs(x) + abs(y)
		if distance <= 4:
			no_transport += 1
	no_transport_percentage = float(no_transport) / number_of_walks
	print("Walk size = {} \% of no transport = {}".format(walk_length, 100*no_transport_percentage))
