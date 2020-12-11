lines = open("input-data.txt", "r").readlines()

columncount = 0
seatid      = 0

for line in lines:
	
	seatdata = [char for char in line.strip()]
	
	rowtotal     = 0
	rowincrement = 64
	
	for rowvalue in list(range(0,7)):
		if seatdata[rowvalue] == 'B':
			rowtotal = rowtotal + rowincrement
			
		rowincrement = rowincrement / 2
	
	seattotal     = 0
	seatincrement = 4	
		
	for rowvalue in list(range(7,10)):
		if seatdata[rowvalue] == 'R':
			seattotal = seattotal + seatincrement
			
		seatincrement = seatincrement / 2
		
	if seatid < rowtotal * 8 + seattotal:
		seatid = rowtotal * 8 + seattotal
				
print("Highest seat ID {}".format(seatid))
