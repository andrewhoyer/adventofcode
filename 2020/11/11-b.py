import copy

inputdata = open("input-data.txt", "r").readlines()

# Get the seating data into an array
seatingplan = []

directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

for line in inputdata:
	rowdata = []
	for char in line.strip():
		rowdata.append(char)
	
	seatingplan.append(rowdata)
	

def numberofoccupiedsurroundingseats(checkrow, checkcol):
	
	occupied = 0
	
	for i in range(checkrow - 1, checkrow + 2):
		for j in range(checkcol - 1, checkcol + 2):
			if i >= 0 and i <= len(tempseatingplan) - 1 and j >= 0 and j <= len(tempseatingplan[checkrow]) - 1:
				if j == checkcol and i == checkrow:
					pass
				else:
					if tempseatingplan[i][j] == "#":
						print
						occupied = occupied + 1	
	
	return occupied
	
def numberofoccupiedseatsinsight(checkrow, checkcol):
	
	occupied = 0

	for direction in directions:
		
		exist = False
		i     = checkrow
		j     = checkcol
		
		while exist == False:
			i = i + direction[0]
			j = j + direction[1]
			
			if i < 0 or j < 0 or i > len(seatingplan) - 1 or j > len(seatingplan[0]) - 1:
				break
			else:
				if tempseatingplan[i][j] == "#":
					occupied = occupied + 1
					exist = True
				elif  tempseatingplan[i][j] == "L":
					exist = True
					
	return occupied 

nochanges = False

tempseatingplan = []

counter = 0

while nochanges == False:
	
	# Use deepcopy to duplicate the list
	tempseatingplan = copy.deepcopy(seatingplan)
	
	changesmade = 0
	
	for row in range(0, len(tempseatingplan)):
		for col in range(0, len(tempseatingplan[row])):
			if tempseatingplan[row][col] == "L":
				if numberofoccupiedseatsinsight(row, col) == 0:
					seatingplan[row][col] = "#"
					changesmade = changesmade + 1
					
			elif tempseatingplan[row][col] == "#":
				if numberofoccupiedseatsinsight(row, col) >= 5:
					seatingplan[row][col] = "L"
					changesmade = changesmade + 1


	"""
	# Outputs the full seating plan
	for line in seatingplan:
		row = ""
		for char in line:
			row = row + char
	
		print("{}".format(row))

	print("\n")
	"""
	
	if changesmade == 0:
		nochanges = True

	#if counter == 2:
	#	nochanges = True;
	
		
	counter = counter + 1
	

occupied = 0

for line in seatingplan:
		for seat in line:
			if seat == "#":
				occupied = occupied + 1

print("\nOccupied seats: {}".format(occupied))
