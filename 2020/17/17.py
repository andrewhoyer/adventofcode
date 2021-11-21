import copy

inputdata = open("input-data.txt", "r").readlines()

# Returns the minimum and maximum values of any given dimension
def findminmaxdimensions(dimension):

	minmax = {"x": {"min":0,"max":0}, "y": {"min":0,"max":0}, "z": {"min":0,"max":0} }
	
	for gridkey in dimension:
		if dimension[gridkey]["x"] < minmax["x"]["min"]:
			minmax["x"]["min"] = dimension[gridkey]["x"]
			
		if dimension[gridkey]["x"] > minmax["x"]["max"]:
			minmax["x"]["max"] = dimension[gridkey]["x"]
			
		if dimension[gridkey]["y"] < minmax["y"]["min"]:
			minmax["y"]["min"] = dimension[gridkey]["y"]
			
		if dimension[gridkey]["y"] > minmax["y"]["max"]:
			minmax["y"]["max"] = dimension[gridkey]["y"]
			
		if dimension[gridkey]["z"] < minmax["z"]["min"]:
			minmax["z"]["min"] = dimension[gridkey]["z"]
			
		if dimension[gridkey]["z"] > minmax["z"]["max"]:
			minmax["z"]["max"] = dimension[gridkey]["z"]
			
	return minmax

# Displays the dimension in layers. Useful for debugging.
def displaydimension(dimension, minmax):
	
	for grid_z in range(minmax["z"]["min"], minmax["z"]["max"] + 1):
		
		for grid_y in range(minmax["y"]["min"], minmax["y"]["max"] + 1):
			
			rowstring = ""
			for grid_x in range(minmax["x"]["min"], minmax["x"]["max"] + 1):
				
				thiskey = "{}|{}|{}".format(grid_x, grid_y, grid_z)
				
				if thiskey in dimension:
					rowstring = rowstring + "#"
				else:
					rowstring = rowstring + "."
					
			print(rowstring)

		print("\n------\n")
		
		
# Set up initial list of active cubes

pocketdimension = {}

grid_z = 0
grid_x = 0
grid_y = 0

for line in inputdata:
	
	for char in line.strip():
		
		if char == "#":
	
			thiskey = "{}|{}|{}".format(grid_x, grid_y, grid_z)
			if thiskey not in pocketdimension:
				pocketdimension[thiskey] = {"state":"active", "x": grid_x, "y": grid_y, "z": grid_z, "neighbors": 0}
		
		grid_x = grid_x + 1
		
	grid_y = grid_y + 1
	grid_x = 0


for cycle in range(0, 6):
	
	# Create a copy to work on
	temppocketdimension = copy.deepcopy(pocketdimension)
	
	for gridkey in pocketdimension:

		for check_z in range(pocketdimension[gridkey]['z'] - 1, pocketdimension[gridkey]['z'] + 2):
			for check_x in range(pocketdimension[gridkey]['x'] - 1, pocketdimension[gridkey]['x'] + 2):
				for check_y in range(pocketdimension[gridkey]['y'] - 1, pocketdimension[gridkey]['y'] + 2):
					#print ("looking at x{}, y{}, z{}".format(check_x, check_y, check_z))
					if check_z == pocketdimension[gridkey]['z'] and check_x == pocketdimension[gridkey]['x'] and check_y == pocketdimension[gridkey]['y']:
						# Center item, ignore
						pass
					else:
						cube_key = "{}|{}|{}".format(check_x, check_y, check_z)
						if cube_key in pocketdimension:
							if pocketdimension[cube_key]["state"] == "active":
								# Active cubes
								#print("Active neighbour: {}".format(cube_key))
								temppocketdimension[gridkey]["neighbors"] += 1
							else:
								# Inactive cubes
								#print("Inactive neighbour: {}".format(cube_key))
								if cube_key in temppocketdimension:
									temppocketdimension[cube_key]["neighbors"] += 1
								else:
									temppocketdimension[cube_key] = {"state":"inactive", "x": check_x, "y": check_y, "z": check_z, "neighbors": 1}
							
						else:
							# Inactive cubes
							#print("Inactive neighbour (2): {}".format(cube_key))
							if cube_key in temppocketdimension:
								temppocketdimension[cube_key]["neighbors"] += 1
							else:
								temppocketdimension[cube_key] = {"state":"inactive", "x": check_x, "y": check_y, "z": check_z, "neighbors": 1}	
							
	
	for gridkey in list(temppocketdimension.keys()):
		if temppocketdimension[gridkey]["state"] == "active":
			if temppocketdimension[gridkey]["neighbors"] == 2 or temppocketdimension[gridkey]["neighbors"] == 3:
				temppocketdimension[gridkey]["neighbors"] = 0
			else:
				temppocketdimension.pop(gridkey)
		else:
			if temppocketdimension[gridkey]["neighbors"] == 3:
				temppocketdimension[gridkey]["state"] = "active"
				temppocketdimension[gridkey]["neighbors"] = 0
			else:
				temppocketdimension.pop(gridkey)
	
	
	# Copy the temp dimension to the permanent one
	pocketdimension = copy.deepcopy(temppocketdimension)
	
	# For debugging
	#displaydimension(pocketdimension, findminmaxdimensions(pocketdimension))


# Result
print(len(pocketdimension))
