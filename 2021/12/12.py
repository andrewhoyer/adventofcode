def searchcavepath(cave, newhistory, connections, depth):
	
	depth += 1
	
	# For readability in nested output
	debugspacing = "     " * depth

	#print("{}CURRENTLY in cave: {}".format(debugspacing, cave))  

	# Copy the history so each iteration uses its own path
	thishistory = newhistory.copy()
	thishistory.append(cave)
	
	pathcount = 0
	
	# Return immediately if the current path is 'end'
	if cave == 'end':
		#print('{}EXIT, history: {}'.format(debugspacing, thishistory))
		pathcount += 1	
		return pathcount
	
	# Loop through each possible connection from the current room
	for room in connections[cave]:
		
		# Ignore the start as well as the current room
		if room == 'start' or room == cave:
			continue
			
		elif room == room.lower() and room in thishistory:
			# If the room is lower cased, ignore it if it's already in the history
			continue
		
		else:
			# Explore the next cave
			pathcount += searchcavepath(room, thishistory, connections, depth)
	
	return pathcount
	

if __name__ == "__main__":
	
	inputdata = open("input-data.txt", "r").readlines()
	
	# Build a dictionary of each cave and all connections from each cave
	connections = {}
	
	for row in inputdata:
		
		room1, room2 = row.strip().split("-")
		
		if room1 in connections:
			if room2 not in connections[room1]:
				connections[room1].append(room2)
			
		else:
			connects = []
			connects.append(room2)
			connections[room1] = connects
			
		if room2 in connections:
			if room1 not in connections[room2]:
				connections[room2].append(room1)
			
		else:
			connects = []
			connects.append(room1)
			connections[room2] = connects
	
	
	# Fire up the recurring function
	history = []
	numberofpaths = searchcavepath('start', history, connections, 0)
	
	print("Number of possible paths: {}".format(numberofpaths))
	
	exit()
	