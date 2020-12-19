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
waypointposition = [10,1]
waypointquadrant = 0; # From top-right moving clockwise, 0, 1, 2, 3
	
for line in inputdata:

	action = re.search(r'(.{1})', line).group()
	amount = int(re.search(r'([0-9]+)', line).group())

	if action == 'N':
		waypointposition[1] = waypointposition[1] + amount
	elif action == 'E':
		waypointposition[0] = waypointposition[0] + amount
	elif action == 'S':
		waypointposition[1] = waypointposition[1] - amount
	elif action == 'W':
		waypointposition[0] = waypointposition[0] - amount
	elif action == 'L':

		step = int(amount / 90)
		
		waypointrelative = []
		
		if waypointquadrant == 0:
			diffx = waypointposition[0] - currentposition[0]
			diffy = waypointposition[1] - currentposition[1]
			
			if step == 1:
				waypointrelative = [diffy * -1, diffx] # To Quadrant 1
			elif step == 2:
				waypointrelative = [diffx * -1, diffy * -1] # To Quadrant 2
			elif step == 3:
				waypointrelative = [diffy, diffx * -1] # To Quadrant 3
			
		elif waypointquadrant == 1:
			diffx = waypointposition[0] - currentposition[0]
			diffy = currentposition[1] - waypointposition[1]			

			if step == 1:
				waypointrelative = [diffy, diffx] # To Quadrant 0
			elif step == 2:
				waypointrelative = [diffx * -1, diffy] # To Quadrant 3	
			elif step == 3:
				waypointrelative = [diffy * -1, diffx * -1] # To Quadrant 2
			
		elif waypointquadrant == 2:
			diffx = currentposition[0] - waypointposition[0]
			diffy = currentposition[1] - waypointposition[1]

			if step == 1:
				waypointrelative = [diffy, diffx * -1] # To Quadrant 1
			elif step == 2:
				waypointrelative = [diffx, diffy] # To Quadrant 0	
			elif step == 3:
				waypointrelative = [diffy * -1, diffx]	# To Quadrant 3
						
		elif waypointquadrant == 3:
			diffx = currentposition[0] - waypointposition[0]
			diffy = waypointposition[1] - currentposition[1]
		
			if step == 1:
				waypointrelative = [diffy * -1, diffx * -1] # To Quadrant 2
			elif step == 2:
				waypointrelative = [diffx, diffy * -1] # To Quadrant 1
			elif step == 3:
				waypointrelative = [diffy, diffx]	# To Quadrant 0
		
		waypointposition[0] = currentposition[0] + waypointrelative[0]
		waypointposition[1] = currentposition[1] + waypointrelative[1]
			
	elif action == 'R':
	
		step = int(amount / 90)
		
		waypointrelative = []
		
		if waypointquadrant == 0:
			diffx = waypointposition[0] - currentposition[0]
			diffy = waypointposition[1] - currentposition[1]
			
			if step == 1:
				waypointrelative = [diffy, diffx * -1] # To Quadrant 1
			elif step == 2:
				waypointrelative = [diffx * -1, diffy * -1] # To Quadrant 2
			elif step == 3:
				waypointrelative = [diffy * -1, diffx] # To Quadrant 3
			
		elif waypointquadrant == 1:
			diffx = waypointposition[0] - currentposition[0]
			diffy = currentposition[1] - waypointposition[1]			

			if step == 1:
				waypointrelative = [diffy * -1, diffx * -1] # To Quadrant 2
			elif step == 2:
				waypointrelative = [diffx * -1, diffy] # To Quadrant 3	
			elif step == 3:
				waypointrelative = [diffy, diffx] # To Quadrant 0
			
		elif waypointquadrant == 2:
			diffx = currentposition[0] - waypointposition[0]
			diffy = currentposition[1] - waypointposition[1]

			if step == 1:
				waypointrelative = [diffy * -1, diffx] # To Quadrant 3
			elif step == 2:
				waypointrelative = [diffx, diffy] # To Quadrant 0	
			elif step == 3:
				waypointrelative = [diffy, diffx * -1]	# To Quadrant 1
						
		elif waypointquadrant == 3:
			diffx = currentposition[0] - waypointposition[0]
			diffy = waypointposition[1] - currentposition[1]
		
			if step == 1:
				waypointrelative = [diffy, diffx] # To Quadrant 0
			elif step == 2:
				waypointrelative = [diffx, diffy * -1] # To Quadrant 1
			elif step == 3:
				waypointrelative = [diffy * -1, diffx * -1]	# To Quadrant 2
		
		waypointposition[0] = currentposition[0] + waypointrelative[0]
		waypointposition[1] = currentposition[1] + waypointrelative[1]		
			
	elif action == 'F':
		
		movex = 0
		movey = 0
		
		if currentposition[0] >= waypointposition[0]:
		  movex = (currentposition[0] - waypointposition[0]) * -1
		else:
		  movex = waypointposition[0] - currentposition[0]
		  
		if currentposition[1] >= waypointposition[1]:
			movey = (currentposition[1] - waypointposition[1]) * -1
		else:		
			movey = waypointposition[1] - currentposition[1]
		
		currentposition[0] = currentposition[0] + (movex * amount)
		currentposition[1] = currentposition[1] + (movey * amount)
		
		waypointposition[0] = waypointposition[0] + (movex * amount)
		waypointposition[1] = waypointposition[1] + (movey * amount)
			
	#print("current position: {}, waypoint position {}".format(currentposition, waypointposition))

print(abs(currentposition[0]) + abs(currentposition[1]))