
def totaldifference(diff):
	
	total = 0
	addthis = 1
	
	total += int(((diff * (diff + 1)) / 2))
	
	addthis += 1
	
	return total


if __name__ == "__main__":
	
	inputdata = open("input-data.txt", "r").read()
	
	originaldata = inputdata.split(",")
	
	highestposition = 0
	
	alignments = []
	for item, crab in enumerate(originaldata):
		thisposition = int(originaldata[item])
		alignments.append(thisposition)
		
		if thisposition > highestposition:
			highestposition = thisposition
	
	leastfuel = -1
	
	for checkposition in range(0,highestposition):

		#print("checkposition {}, crab {}".format(checkposition, crab))
		fuelused = 0
		
		for crab in alignments:
			#print("\n\n------------------\n\n")

			
			if checkposition == crab:
				#print("skip")
				continue
			

			if checkposition < crab:
				fuelused += totaldifference(crab - checkposition)
			elif checkposition > crab:
				fuelused += totaldifference(checkposition - crab)
			elif checkposition == crab:	
				fuelused += 0
			
		if leastfuel == -1:
			leastfuel = fuelused
		else:
			if fuelused < leastfuel:
				leastfuel = fuelused
	
		#print("least {}".format(leastfuel))
	
	
	print(leastfuel)
	
	exit()
	