from math import e
import sys
import time
import pprint
pp = pprint.PrettyPrinter(indent=2)

argv1 = sys.argv[1] # Filename of puzzle data passed as parameter

inputdata = open(argv1, "r").readlines()

# Get the first line which contains instructions
instructions = inputdata.pop(0).strip()

# Remove the next line which is blank
inputdata.pop(0)

move_list = {}
destinations = []
for line in inputdata:
        parts = line.strip().split(" = ")
        if parts[0][2] == "A":
            destinations.append(parts[0])
        move_list[parts[0]] = parts[1].replace("(", "").replace(")", "").replace(",", "").split(" ")


def check_destinations(destinations):
    for dest in destinations:
        if dest[2] != "Z":
            return False
        
    return True


denominators = []

for destination in destinations:
    
    counter = 1
    flag = False
    
    temp_dest = destination 

    while flag == False:
        
        for ch in instructions:
            if ch == "R":
                temp_dest = move_list[temp_dest][1]
            else:
                temp_dest = move_list[temp_dest][0]
            
            if temp_dest[2] == "Z":
                flag = True
                denominators.append(counter)
                break

            counter += 1
     

lastdepth = {} # Records the first minute any one depth is reached

# Records the difference between when each depth is matched. This is the key to my
# solution, as I realized that matches are achieved at exact intervals.
intervals = {}

# The recursive function. Parameters:
# comparearray - the list of values
# common - the value to be evaluated
# depth - the recursion depth
# increaseby - the key! Each iteration tells the next one what to return if it fails

def comparenextvalue(comparearray, common, depth, increaseby):
	
	# Indenting really helps with debugging, to show search depth level
	spaces = ''
	for _ in range(depth):
		spaces = spaces + '  '
		
	# Checks to see if the value matches, in which case it divides evenly
	mod = common % comparearray[depth]

	if mod == 0:
		
		# Check the next iteration, unless it's the last item in the array
		if depth < len(comparearray) - 1:
			
			if depth in lastdepth:
				if depth not in intervals:
					# Record the interval only once
					intervals[depth] = common - lastdepth[depth]
				
				# The key! See function description.
				return comparenextvalue(comparearray, common, depth + 1, intervals[depth])
				
			else:
				# Record the minute the first time any depth is reached
				lastdepth[depth] = common
				
				return comparenextvalue(comparearray, common, depth + 1, increaseby)
			
		else:
			# Reached the end of the array, and the puzzle is solved
			return 0
			
	else:
		# If it's not a match, simply send back the number of minutes to increase.
		# This is how the script reaches the solution so quickly.			
		return common + increaseby




# Set the offset for the common denominator
common = denominators[0]

exitLoop = False;

while exitLoop == False:

	increaseToValue = comparenextvalue(denominators, common, 0, denominators[0])
	
	if increaseToValue == 0:
		print(f"Part 2 solution: {common}")
		exitLoop = True
	else:
		common = increaseToValue

exit()
