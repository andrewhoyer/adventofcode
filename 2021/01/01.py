inputdata = open("input-data.txt", "r").readlines()

current = 0

depthincreases = 0

for depth in inputdata:
	
	nextdepth = int(depth.strip())
	
	if current == 0:
		current = nextdepth
	else:
		if nextdepth > current:
			depthincreases += 1
		
		current = nextdepth
	

print("Increases: {}".format(depthincreases))
