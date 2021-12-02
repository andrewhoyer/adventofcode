inputdata = open("input-data.txt", "r").readlines()

#print(inputdata);

depthincreases = 0

counter = 0

for depth in inputdata:
	
	currentdepth = int(inputdata[counter].strip()) + int(inputdata[counter+1].strip()) + int(inputdata[counter+2].strip())
	nextdepth = int(inputdata[counter+1].strip()) + int(inputdata[counter+2].strip()) + int(inputdata[counter+3].strip())
	
	if nextdepth > currentdepth:
		depthincreases += 1

	counter += 1	
	
	if counter >= len(inputdata) - 3:
		break

print("Increases: {}".format(depthincreases))
