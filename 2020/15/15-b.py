inputdata  = [2,0,6,12,1,3]
positions  = {}
lastspoken = 0
difference = 0
counter    = 0

# Iterate through the input data to set up the starting array
for input in inputdata:
	counter = counter + 1
	
	# For each number, track the last two times it appears in the array
	# Initially, these are set to the same value
	positions[input] = [counter, counter]
	lastspoken = input
	
# Find the 30 millionth number in the sequence
while counter < 30000000:
		
	# Check to see if the next number in the sequence is already in the list
	if lastspoken in positions:
		
		# If it matches the last one, use zero
		if positions[lastspoken][0] == counter:
			lastspoken = 0
			
		else:	
			# Find the difference between the current position and the second last time the number appeared
			lastspoken = counter - positions[lastspoken][0]
		
	else:
		# If not present, use zero
		lastspoken = 0
		
	counter = counter + 1		
		
	# Check the list again with the next number and add or update
	if lastspoken in positions:
		latest = positions[lastspoken][1]
		positions[lastspoken][0] = latest
		positions[lastspoken][1] = counter
		
	else:
		positions[lastspoken] = [counter, counter]
	
print("The last number spoken is: {}\n\n".format(lastspoken,))
