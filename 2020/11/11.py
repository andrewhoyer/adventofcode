import copy

inputdata = open("input-data.txt", "r").readlines()

# Get the seating data into an array
seatingplan = []

for line in inputdata:
	rowdata = []
	for char in line.strip():
		rowdata.append(char)
	
	seatingplan.append(rowdata)
	

def numberofoccupiedsurroundingseats(checkrow, checkcol):
	#print("checkrow {} checkcol {}".format(checkrow, checkcol))		
	occupied = 0
	
	for i in range(checkrow - 1, checkrow + 2):
		for j in range(checkcol - 1, checkcol + 2):
			if i >= 0 and i <= len(tempseatingplan) - 1 and j >= 0 and j <= len(tempseatingplan[checkrow]) - 1:
				if j == checkcol and i == checkrow:
					pass
				else:
					#print("i {} j {}".format(i, j))		
					if tempseatingplan[i][j] == "#":
						print
						occupied = occupied + 1
		
	return occupied 

nochanges = False

tempseatingplan = []

while nochanges == False:
	
	# Use deepcopy to duplicate the list
	tempseatingplan = copy.deepcopy(seatingplan)
	
	changesmade = 0
	
	for row in range(0, len(tempseatingplan)):
		for col in range(0, len(tempseatingplan[row])):
			if tempseatingplan[row][col] == "L":
				if numberofoccupiedsurroundingseats(row, col) == 0:
					seatingplan[row][col] = "#"
					changesmade = changesmade + 1
					
			elif tempseatingplan[row][col] == "#":
				if numberofoccupiedsurroundingseats(row, col) >= 4:
					seatingplan[row][col] = "L"
					changesmade = changesmade + 1

	"""
	# Outputs the full seating plan
	for line in seatingplan:
		row = ""
		for char in line:
			row = row + char
		
		print("{}".format(row))
	"""
	
	if changesmade == 0:
		nochanges = True
	
occupied = 0

for line in seatingplan:
		for seat in line:
			if seat == "#":
				occupied = occupied + 1

print("\nOccupied seats: {}".format(occupied))
