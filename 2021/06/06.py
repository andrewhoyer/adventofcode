if __name__ == "__main__":
	
	inputdata = open("input-data2.txt", "r").read()
	
	originaldata = inputdata.split(",")
	
	lanternfish = []
	for item, fish in enumerate(originaldata):
		lanternfish.append(int(originaldata[item]))
	
	print(lanternfish)

	diffday = 0
	for day in range(0, 80):
		
		startingfish = len(lanternfish)
		
		fishtoadd = 0
		
		for item, fish in enumerate(lanternfish):
			
			lanternfish[item] -= 1
			
			if lanternfish[item] < 0:
				lanternfish[item] = 6
				fishtoadd += 1
				
		
		if fishtoadd > 0:
			for n in range(0,fishtoadd):
				lanternfish.append(8)
		
		endingfish =  len(lanternfish)
		
		#print("{} - {} - {}".format(len(lanternfish), endingfish - startingfish, (endingfish - startingfish) / startingfish	 ))
	
	print(len(lanternfish))
			

	exit()

