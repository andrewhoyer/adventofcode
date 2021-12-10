if __name__ == "__main__":
	
	inputdata = open("input-data.txt", "r").readlines()
	
	counter = 0
	for lines in inputdata:
		
		outputdigits = lines.strip().split(" | ")[1].split(" ")
		
		for onedigit in outputdigits:
			if len(onedigit) in [2, 3, 4, 7]:
				counter += 1
				
	print(counter)
	
	exit()
