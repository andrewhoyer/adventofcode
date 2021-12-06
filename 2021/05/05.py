if __name__ == "__main__":
	
	inputdata = open("input-data.txt", "r").readlines()

	# This script solves the puzzle in two parts. The entire process is run
	# twice, once without processing diagonals, and once with them. 
	
	processdiagonals = False
	
	for _ in range(0,2):
		
		# A dictionary to contain the coordinate data of plotted points
		positions = {}

		for row in inputdata:
			
			coords = row.strip().split(" -> ")
			
			starting = coords[0].split(",")
			ending = coords[1].split(",")
		
			# Determine the type of row being processed
			
			if starting[0] == ending[0]:
				# Vertical lines
				
				endvalue = int(ending[1])
				step = 1
				
				if int(starting[1]) > endvalue:
					step = -1
					endvalue -= 1
				else:
					endvalue += 1
				
				for y in range(int(starting[1]), endvalue, step):
					
					if "{},{}".format(starting[0], y) in positions:
						positions["{},{}".format(starting[0], y)] += 1
					else:
						positions["{},{}".format(starting[0], y)] = 1
				
			elif starting[1] == ending[1]:
				# Horizontal lines
				
				endvalue = int(ending[0])
				step = 1
				
				if int(starting[0]) > endvalue:
					step = -1
					endvalue -= 1
				else:
					endvalue += 1
				
				for x in range(int(starting[0]), endvalue, step):
					
					if "{},{}".format(x, starting[1]) in positions:
						positions["{},{}".format(x, starting[1])] += 1
					else:
						positions["{},{}".format(x, starting[1])] = 1
			else:
				# Diagonals
				# Only run the second time around for Part 2
				
				if processdiagonals == True:
			
					startx = int(starting[0])
					endx = int(ending[0])
			
					starty = int(starting[1])
					endy = int(ending[1])
			
					stepx = 1
					if startx > endx:
						stepx = -1
			
					stepy = 1
					if starty > endy:
						stepy = -1
					
					# Move through the diagonal path
					while startx != endx and starty != endy:
							
						if "{},{}".format(startx, starty) in positions:
							positions["{},{}".format(startx, starty)] += 1
						else:
							positions["{},{}".format(startx, starty)] = 1
					
						startx += stepx
						starty += stepy
				
					if "{},{}".format(startx, starty) in positions:
						positions["{},{}".format(startx, starty)] += 1
					else:
						positions["{},{}".format(startx, starty)] = 1
				
			
		if processdiagonals == False:
			print("Puzzle Part 1")
		else:
			print("Puzzle Part 2")
		
		counter = 0
		for keyposition in list(positions.keys()):
			if positions[keyposition] >= 2:
				counter += 1
		
		print("Positions with overlapping points: {}\n".format(counter))
		
		processdiagonals = True
		