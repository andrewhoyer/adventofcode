inputdata = open("input-data2.txt", "r").readlines()


buses = []

minute = 0
	
for bus in inputdata[1].strip().split(','):

	if bus == 'x':
		pass
	else:
		buses.append({'bus': int(bus), 'minute': minute})
		minute = 0
		
	minute = minute + 1


print(buses)

#exit()

def comparenextbus(busarray, minute, depth):
	
	# Indenting really helps with debugging, to show search depth level
	spaces = ''
	for _ in range(depth):
		spaces = spaces + '  '

	#if depth > 0:
		#print("\n{}Checking bus {}, minute {}, depth {}".format(spaces,busarray[depth], minute, depth))

	mod = minute % busarray[depth]['bus']

	if mod == 0:
	
		#print("{}Found a match for bus {}, minute {}".format(spaces, busarray[depth], minute))
		if depth < len(busarray) - 1:
			#print("{} Not yet at end of array. Look at depth {} and compare for this many minutes later {}".format(spaces, depth + 1, busarray[depth + 1]['minute']))
			return comparenextbus(busarray, minute + busarray[depth + 1]['minute'], depth + 1)
		else:
			#print("{} Reached the end of array".format(spaces))
			return True
	else:
		# Not a match
		return False

	
exit = False;

minute = 0

while exit == False:

	if comparenextbus(buses, minute, 0) == True:
		print("Earliest minute {}".format(minute))
		exit = True

	minute = minute + buses[0]['bus']
	
	
	#if minute > 1068781:
	#	exit = True
