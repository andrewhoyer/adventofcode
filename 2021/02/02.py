inputdata = open("input-data.txt", "r").readlines()

depth = 0
horizontal = 0

for movement in inputdata:
	
	movementparts = movement.strip().split(" ")
	
	if movementparts[0] == 'forward':
		horizontal += int(movementparts[1])
	elif movementparts[0] == 'up':
		depth -= int(movementparts[1])
	elif movementparts[0] == 'down':
		depth += int(movementparts[1])

print("Horiz: {}, Depth: {}, Multiplied: {}".format(horizontal, depth, horizontal * depth))
