def searchcavepath(cave, history, connections, depth, exploredtwice):
	
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
		
		# Ignore the start as well as the current room
		if potentialcave == 'start' or potentialcave == cave:
			continue
		
		# Special consideration for lower cased caves	
		elif potentialcave == potentialcave.lower():
			
			# Handle whether or not the lower case cave is in the history
			if potentialcave in thishistory:
				
				# Allow for a path to have a single duplicate lower case cave
				if exploredtwice == False:
					pathcount += searchcavepath(potentialcave, thishistory, connections, depth, True)
				else:
					continue
				
			# If the lower case cave is not already in the history, explore it
			else:
				pathcount += searchcavepath(potentialcave, thishistory, connections, depth, exploredtwice)
		
		else:
			# All other cases, explore the next cave
			pathcount += searchcavepath(potentialcave, thishistory, connections, depth, exploredtwice)
	
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
	
	#print(connections)
	
	# Fire up the recurring function
	
	numberofpaths = searchcavepath('start', [], connections, 0, False)
	
	print("Number of possible paths: {}".format(numberofpaths))
	
	exit()
	