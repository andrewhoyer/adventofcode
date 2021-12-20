if __name__ == "__main__":
	
	inputdata = open("input-data.txt", "r").read()
	
	sections = inputdata.split("\n\n")
	
	# Build array of dots from first section in puzzle data
	dots = []
	
	for row in sections[0].split("\n"):
		x, y = row.split(",")
		dots.append("{},{}".format(x, y))
		
	# Build list of instructions from second section in puzzle data
	instructions = []
	
	for instruction in sections[1].split("\n"):
		useless, actualinstruction = instruction.split(" along ")
		direction, foldrow = actualinstruction.split("=")
		instructions.append({"direction": direction, "foldrow": int(foldrow)})
	
	# A flag to output Par 1 data
	outputfirstpuzzle = True
	
	# Process each instruction, folding by y or x
	# The core principal here is simply to move every point by x or y based on
	# the fold direction. Duplicates are ignored and dealt with later
	for instruction in instructions:
		
		for rowindex, row in enumerate(dots):
			
			x, y = row.split(",")
			x = int(x)
			y = int(y)
			
			if instruction['direction'] == "y":
				if y > instruction['foldrow']:
					y = instruction['foldrow'] - (y - instruction['foldrow'])
					
					dots[rowindex] = "{},{}".format(x, y)
					
			if instruction['direction'] == "x":
				if x > instruction['foldrow']:
					x = instruction['foldrow'] - (x - instruction['foldrow'])
					
					dots[rowindex] = "{},{}".format(x, y)
		
		# Strip out duplicates
		uniquedots = []
	
		for thisdot in dots:
			if thisdot not in uniquedots:
				uniquedots.append(thisdot)		
		
		dots = uniquedots
		
		if outputfirstpuzzle == True:
			print("Part 1: {}".format(len(dots)))
			outputfirstpuzzle = False
	
	# Calculate the maximum range of the dots grid
	highx = 0
	highy = 0
	
	for thisdot in dots:
		x, y = thisdot.split(",")
		x = int(x)
		y = int(y)
		
		if x > highx:
			highx = x
			
		if y > highy:
			highy = y
	
	# Create a text printout of the grid for the part 2 answer
	print("Part 2:")
	for thisy in range(0, highy + 1):	
		rowstring = ""
		for thisx in range(0, highx + 1):
			if "{},{}".format(thisx, thisy) in uniquedots:
				rowstring += "#"
			else:
				rowstring += "."
				
		print(rowstring)
	
	exit()