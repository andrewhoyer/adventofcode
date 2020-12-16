inputdata = open("input-data.txt", "r").readlines()

complete = False
position = 25
lookback = 25
nonsum   = 0

while position <= len(inputdata) - 1 and complete == False:
	print("\n--------------------\n")
	foundmatchingpair = False

	counter = 1
			
	for upto25 in range(position - 25, position):
		
		firstnumber = int(inputdata[upto25].strip())
		

		
		for i in range(position - 25 + counter, position):

			if int(inputdata[position].strip()) == int(inputdata[upto25].strip()) + int(inputdata[i].strip()):
				print("{} + {} = {}".format(int(inputdata[upto25].strip()),int(inputdata[i].strip()), int(inputdata[position].strip())))
				foundmatchingpair = True
				break		
			else:
				print("X {} + {} = {}".format(int(inputdata[upto25].strip()),int(inputdata[i].strip()), int(inputdata[position].strip())))
				
		counter = counter + 1
				
		if foundmatchingpair:
			break
			
	if foundmatchingpair == False:
		complete = True
	else:
		position = position + 1

"""
  firstnumber = int(numbers.pop().strip())

  for number in numbers:
    if firstnumber + int(number.strip()) == 2020:
      secondnumber = int(number.strip())
      complete = True

  if len(numbers) <= 1:
    complete = True
    

"""

print("Position {}, Value {}".format(position, inputdata[position].strip()))

