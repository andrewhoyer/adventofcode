inputdata = open("input-data.txt", "r").readlines()

complete = False
startposition = 0

targetsum = 248131121

while startposition < len(inputdata) - 1 and complete == False:
#	print("\n--------------------\n")

	foundasum = False
	position = startposition

	entries = []
	sum = 0
			
	while position < len(inputdata) - 1 and foundasum == False:
		
		
		nextnumber = int(inputdata[position].strip())
		
		entries.append(nextnumber)
		sum = sum + nextnumber
		
		if sum > targetsum:
			break
			
		if sum == targetsum:
			foundasum = True
			print("Found a set of numbers that equals {}, Start position {}, End Position {}, entries array: {}".format(targetsum, startposition, position, entries))
			break
					
		position = position + 1
	
	
	
							
	if foundasum == True:
		complete = True
		break
	else:
		startposition = startposition + 1
		
		
		

"""
  firstnumber = int(numbers.pop().strip())

  for number in numbers:
    if firstnumber + int(number.strip()) == 2020:
      secondnumber = int(number.strip())
      complete = True

  if len(numbers) <= 1:
    complete = True
    

"""
# Sort! Important as reqs ask for highest and lowest, not first and last in the list
entries = sorted(entries)

print("\nLowest value {} + Highest Value {} = {}\n".format(entries[0], entries[len(entries) - 1], entries[0] + entries[len(entries) - 1]))

