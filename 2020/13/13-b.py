inputdata = open("input-data.txt", "r").readlines()


buses = [] # Store the bus data in an array

lastdepth = {} # Records the first minute any one depth is reached

# Records the difference between when each depth is matched. This is the key to my
# solution, as I realized that matches are achieved at exact intervals.
intervals = {}

# Set number of minutes between busses
setminute = 0
	
for bus in inputdata[1].strip().split(','):

	if bus == 'x':
		pass
	else:
		buses.append({'bus': int(bus), 'minute': setminute})
		
	setminute = setminute + 1

#print(buses) # Debug to check to make sure data is formatted correctly

# The recursive function. Parameters:
# busarray - the list of bus data
# minute - the minute of the first bus, which each bus compares itself to
# depth - the recursion depth
# increaseby - the key! Each iteration tells the next one what to return if it fails

def comparenextbus(busarray, minute, depth, increaseby):
	
	# Indenting really helps with debugging, to show search depth level
	spaces = ''
	for _ in range(depth):
		spaces = spaces + '  '

	#print("{}Checking bus {}, minute {}, depth {}".format(spaces, busarray[depth], minute, depth))

	# Checks to see if the bus time matches, in which case it divides evenly
	mod = (minute + busarray[depth]['minute']) % busarray[depth]['bus']

	if mod == 0:
		
		# Check the next iteration, unless it's the last item in the array
		if depth < len(busarray) - 1:
			
			if depth in lastdepth:
				if depth not in intervals:
					# Record the interval only once
					intervals[depth] = (minute + buses[depth]['minute']) - lastdepth[depth]
				
				# The key! See function description.
				return comparenextbus(busarray, minute, depth + 1, intervals[depth])
				
			else:
				# Record the minute the first time any depth is reached
				lastdepth[depth] = minute + buses[depth]['minute']
				
				return comparenextbus(busarray, minute, depth + 1, increaseby)
			
		else:
			# Reached the end of the array, and the puzzle is solved
			return 0
			
	else:
		# If it's not a match, simply send back the number of minutes to increase.
		# This is how the script reaches the solution so quickly.			
		return minute + increaseby




# Set the starting point, which is the time the first bus arrives
minute = buses[0]['bus']

exitLoop = False;

while exitLoop == False:

	#if counter == 10:
		#exit()
	increaseToMins = comparenextbus(buses, minute, 0, buses[0]['bus'])
	
	if increaseToMins == 0:
		print("Earliest minute {}".format(minute))
		exitLoop = True
	else:
		minute = increaseToMins
		#print("\nMoving up to minute {}".format(minute))
