import re

inputdata = open("input-data.txt", "r").readlines()

directions = {
	'N': [0,1],
	'E': [1,0],
	'S': [0,-1],
	'W': [-1,0]
}

directionorder = {
	0: 'N',
	1: 'E',
	2: 'S',
	3: 'W'
}

currentposition = [0,0]
currentdirection = 'E'
	
for line in inputdata:

	action = re.search(r'(.{1})', line).group()
	amount = int(re.search(r'([0-9]+)', line).group())

	direction = 0
	if currentdirection == 'N':
		direction = 0
	elif currentdirection == 'E':
		direction = 1
	elif currentdirection == 'S':
		direction = 2
	elif currentdirection == 'W':
		direction = 3

	if action == 'N':
		currentposition[1] = currentposition[1] + amount
	elif action == 'E':
		currentposition[0] = currentposition[0] + amount
	elif action == 'S':
		currentposition[1] = currentposition[1] - amount
	elif action == 'W':
		currentposition[0] = currentposition[0] - amount
	elif action == 'L':
		steps = int(amount / 90)
	
		direction = direction - steps
	
		if direction < 0:
			direction = direction + 4
		
		currentdirection = directionorder[direction]
	
	elif action == 'R':
		steps = int(amount / 90)
			
		direction = direction + steps
		
		if direction > 3:
			direction = direction - 4
			
		currentdirection = directionorder[direction]
			
	elif action == 'F':
		currentposition[0] = currentposition[0] + directions[currentdirection][0] * amount
		currentposition[1] = currentposition[1] + directions[currentdirection][1] * amount

print(abs(currentposition[0]) + abs(currentposition[1]))