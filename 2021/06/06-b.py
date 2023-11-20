if __name__ == "__main__":
	
	inputdata = open("input-data2.txt", "r").read()
	
	originaldata = inputdata.split(",")
	
	lanternfish = []
	for item, fish in enumerate(originaldata):
		lanternfish.append(int(originaldata[item]))
	
	print(lanternfish)

	totalfish = 0

	fishdata = {}
	
	for fish in lanternfish:
		if fish in fishdata:
			print("already have answer for {}".format(fish))
			totalfish += fishdata[fish]
		else:
			print("calculate {}".format(fish))
			lanternfishhistory = [fish]
			#print (lanternfishhistory)	
			for day in range(0, 256):
				#print (lanternfishhistory)	
				#startingfish = len(lanternfishhistory)
		
				fishtoadd = 0
		
				for item, fish in enumerate(lanternfishhistory):
			
					lanternfishhistory[item] -= 1
			
					if lanternfishhistory[item] < 0:
						lanternfishhistory[item] = 6
						fishtoadd += 1
				
		
				if fishtoadd > 0:
					for n in range(0,fishtoadd):
						lanternfishhistory.append(8)
		
				#endingfish =  len(lanternfishhistory)
		
			fishdata[fish] = len(lanternfishhistory)
		
			totalfish += len(lanternfishhistory)
		
		
		#print(fishdata)
		#print("Day {}, Total {}, - {} - {}".format(day, len(lanternfish), endingfish - startingfish, (endingfish - startingfish) / startingfish	 ))
		
		
		print("Total {}".format(totalfish))
	
	print("-----------")
	print(totalfish)
	
	exit()

