inputdata = open("input-data.txt", "r").readlines()

	
arrival = int(inputdata[0].strip())

busid = -1
wait  = -1

earliestbus = -1
earliestwait = 999999999
for shuttle in inputdata[1].strip().split(','):

	if shuttle == 'x':
		continue
	
	busid = int(shuttle)
	
	increment = busid
	
	while increment < arrival:
		increment = increment + busid
		
	wait = increment - arrival	
	
	if wait < earliestwait:
		earliestwait = wait
		earliestbus = busid
		
	print("earliest bus {} wait {}".format(earliestbus, earliestwait))

print("Answer: {}".format(earliestbus * earliestwait))