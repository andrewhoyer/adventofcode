inputdata = open("input-data.txt", "r").readlines()

depth = 0
horizontal = 0
aim = 0

for movement in inputdata:
	
	movementparts = movement.strip().split(" ")
	
	if movementparts[0] == 'forward':
		horizontal += int(movementparts[1])
		depth += (aim * int(movementparts[1]))
	elif movementparts[0] == 'up':
		aim -= int(movementparts[1])
	elif movementparts[0] == 'down':
		aim += int(movementparts[1])

print("Horiz: {}, Depth: {}, Multiplied: {}".format(horizontal, depth, horizontal * depth))
