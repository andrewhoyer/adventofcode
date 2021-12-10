if __name__ == "__main__":
	
	inputdata = open("input-data.txt", "r").read()
	
	originaldata = inputdata.split(",")
	
	alignments = []
	for item, crab in enumerate(originaldata):
		alignments.append(int(originaldata[item]))
	
	leastfuel = -1
	
	for crab in range(0,len(alignments)):
		
		fuelused = 0
		
		for checkcrab in range(0,len(alignments)):
			
			if checkcrab == crab:
				continue
			
			if alignments[checkcrab] < alignments[crab]:
				fuelused += (alignments[crab] - alignments[checkcrab])
			elif alignments[checkcrab] > alignments[crab]:
				fuelused += (alignments[checkcrab] - alignments[crab])				
				
		if leastfuel == -1:
			leastfuel = fuelused
		else:
			if fuelused < leastfuel:
				leastfuel = fuelused
	
	
	
	
	print(leastfuel)
	
	exit()
	