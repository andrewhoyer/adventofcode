def searchcavepath(cave, history, connections, depth):
	
	depth += 1
	
	# For readability in nested output
	debugspacing = "     " * depth

	#print("\n------\n{}CURRENTLY in cave: {}".format(debugspacing, cave))  

	# Copy the history so each iteration uses its own path
	thishistory = history.copy()
	
	# Add current cave to the history
	thishistory.append(cave)
	
	pathcount = 0
	
	# Return immediately if the current cave is 'end'
	if cave == 'end':
		pathcount += 1	
		return pathcount
	
	# Loop through each possible connection from the current cave
	for potentialcave in connections[cave]:
		
		# Ignore the start as well as the current cave
		if potentialcave == 'start' or potentialcave == cave:
			continue
			
		elif potentialcave == potentialcave.lower() and potentialcave in thishistory:
			# If the cave is lower cased, ignore it if it's already in the history
			continue
		
		else:
			# Explore the next cave
			pathcount += searchcavepath(potentialcave, thishistory, connections, depth)
	
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
	numberofpaths = searchcavepath('start', [], connections, 0)
	
	print("Number of possible paths: {}".format(numberofpaths))
	
	exit()
	