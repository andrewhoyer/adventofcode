inputdata = open("puzzle-input.txt", "r").readlines()

priority_score = 0

for row in inputdata:
	row_length = len(row.strip())
	counter    = 0
	item_array = []	
	
	for item in row.strip():
		counter = counter + 1
		
		if counter <= row_length / 2:
			item_array.append(item)
		else:
			if item in item_array:
				# Uses the character number, and  offsets by the puzzle's req
				if item.islower():
					priority_score = priority_score + ord(item) - 97 + 1
				else:
					priority_score = priority_score + ord(item) - 65 + 27

				break

print("Sum of priorities for part 1: {}".format(priority_score))

# Part 2

priority_score = 0
counter        = 1
common         = set()
common_temp    = set()

for row in inputdata:
	if counter == 4:
		counter     = 1
		common      = set()
		common_temp = set()

	if counter == 1:
		for item in row.strip():
			common.add(item)
			
	elif counter == 2 or counter == 3:
		common_temp = set(common)
		common      = set()
		
		for item in row.strip():
			if item in common_temp:
				common.add(item)
		
	if counter == 3:
		for item in common:
			# Uses the character number, and  offsets by the puzzle's req
			if item.islower():
				priority_score = priority_score + ord(item) - 97 + 1
			else:
				priority_score = priority_score + ord(item) - 65 + 27
	
	counter = counter + 1

print("Sum of priorities for part 2: {}".format(priority_score))

exit() 
