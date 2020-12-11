lines = open("input-data.txt", "r").readlines()

seatid = 0
rowarray = []

# Create an array of all possible seats, filled with seat column numbers
for rowcount in list(range(0,128)):
	rowarray.append(list(range(0,8)))

for line in lines:
	
	seatdata = [char for char in line.strip()]
	
	rowtotal = 0
	rowincrement = 64
	
	for rowvalue in list(range(0,7)):
		if seatdata[rowvalue] == 'B':
			rowtotal = rowtotal + rowincrement
			
		rowincrement = rowincrement / 2
	
	seattotal = 0
	seatincrement = 4	
		
	for rowvalue in list(range(7,10)):
		if seatdata[rowvalue] == 'R':
			seattotal = seattotal + seatincrement
			
		seatincrement = seatincrement / 2
	
	# Mark seat taken with a star	
	rowarray[int(rowtotal)][int(seattotal)] = '*'
	
#Loop through all seats, locating the one untaken seat	
for rowcount in list(range(0,128)):
	for seatcount in list(range(0,8)):
		if rowcount > 0 and rowcount < 127:
			if rowarray[rowcount][seatcount] != '*':
				if rowarray[rowcount - 1][seatcount] == '*' and rowarray[rowcount + 1][seatcount] == '*':
					seatid = rowcount * 8 + seatcount
					break
	
print("Your seat ID {}".format(seatid))