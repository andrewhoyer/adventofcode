if __name__ == "__main__":
	
	inputdata = open("input-data.txt", "r").readlines()
	
	octopusmap = []
	
	for row in inputdata:
		#print(row)
		
		rowarray = []
		heightarray = []
		for column in [char for char in row.strip()]:
			#print(column)		
			
			rowarray.append(int(column))
			heightarray.append(0)
			
		octopusmap.append(rowarray)
		
	
	print(octopusmap)
			
			
	#risk = 0
	
	#largestbasins = []
	
	totalflashes = 0
	
	# Do 100 iterations
	step = 1
	while True:
	#for step in range(0,100):
		print(step)
		print(octopusmap)
		# Increase each octopus energy by one
		for rowindex, row in enumerate(octopusmap):
			for colindex, height in enumerate(row):
				octopusmap[rowindex][colindex] += 1
			
			
		
		
		
		repeatninesearch = True
		flashedoctopuses = []
		
		# Loop through the entire octopus array until no more 9's are found.
		while repeatninesearch == True:		
			#print(octopusmap)
			#print(totalflashes)
			repeatninesearch = False
			
			
			
			for rowindex, row in enumerate(octopusmap):
				for colindex, height in enumerate(row):
				
					# If it's a nine, FLASH
					if "{}|{}".format(rowindex, colindex) not in flashedoctopuses:
						
						if octopusmap[rowindex][colindex] > 9:
						
							flashedoctopuses.append("{}|{}".format(rowindex, colindex))
						
							#len(octopusmap) * len(octopusmap[0])):
							if len(flashedoctopuses) == 100: 
								print("Step all flash: {}".format(step))
								exit()
							#print("flashed: {}".format(len(flashedoctopuses)))
							repeatninesearch = True
						
							totalflashes += 1
							octopusmap[rowindex][colindex] = 0
					
							#check up
							if rowindex > 0:
								if "{}|{}".format(rowindex - 1, colindex) not in flashedoctopuses:
									octopusmap[rowindex - 1][colindex] += 1
							
							#check right
							if colindex < len(row) - 1:
								if "{}|{}".format(rowindex, colindex + 1) not in flashedoctopuses:
									octopusmap[rowindex][colindex + 1] += 1
			
							#check down
							if rowindex < len(octopusmap) - 1:
								if "{}|{}".format(rowindex + 1, colindex) not in flashedoctopuses:
									octopusmap[rowindex + 1][colindex] += 1
			
							#check left
							if colindex > 0:
								if "{}|{}".format(rowindex, colindex - 1) not in flashedoctopuses:
									octopusmap[rowindex][colindex - 1] += 1

							#check up left
							if rowindex > 0 and colindex > 0:
								if "{}|{}".format(rowindex - 1, colindex - 1) not in flashedoctopuses:
									octopusmap[rowindex - 1][colindex - 1] += 1
							
							#check up right
							if rowindex > 0 and colindex < len(row) - 1:
								if "{}|{}".format(rowindex - 1, colindex + 1) not in flashedoctopuses:
									octopusmap[rowindex - 1][colindex + 1] += 1

							#check down left
							if rowindex < len(octopusmap) - 1 and colindex > 0:
								if "{}|{}".format(rowindex + 1, colindex - 1) not in flashedoctopuses:
									octopusmap[rowindex + 1][colindex - 1] += 1
									
							#check down right
							if rowindex < len(octopusmap) - 1 and colindex < len(row) - 1:
								if "{}|{}".format(rowindex + 1, colindex + 1) not in flashedoctopuses:
									octopusmap[rowindex + 1][colindex + 1] += 1
								
								
							#print(flashedoctopuses)
			#repeatninesearch = False
			
		print(octopusmap)
		step += 1

	print(totalflashes)				
		
	exit()
		
	'''
			#check up
			if rowindex > 0:
				if floormap[rowindex - 1][colindex] <= height:
					continue
							
			#check right
			if colindex < len(row) - 1:
				if floormap[rowindex][colindex + 1] <= height:
					continue
			
			#check down
			
			if rowindex < len(floormap) - 1 :
				if floormap[rowindex + 1][colindex] <= height:
					continue
			
			#check left
			
			if colindex > 0:
				if floormap[rowindex][colindex - 1] <= height:
					continue
		
			print("found low point on row {} and col {}, value {}".format(rowindex, colindex, height))
			risk += (1 + height)	
		
			basinarea = [[rowindex,colindex]]
			basinunique = ["{},{}".format(rowindex, colindex)]

			
			print(basinarea)
			
			foundnew = True
			
			while foundnew == True:
				
				foundnew = False
				
				for basinindex, basinpoint in enumerate(basinarea):
					
					#check up					
					if basinpoint[0] > 0:
						if floormap[basinpoint[0] - 1][basinpoint[1]] < 9:
							if "{},{}".format(basinpoint[0] - 1, basinpoint[1]) not in basinunique:
								foundnew = True
								basinarea.append([basinpoint[0] - 1, basinpoint[1]])
								basinunique.append("{},{}".format(basinpoint[0] - 1, basinpoint[1]))
							
					#check right

					if basinpoint[1] < len(floormap[0]) - 1:
						if floormap[basinpoint[0]][basinpoint[1] + 1] < 9:
							if "{},{}".format(basinpoint[0], basinpoint[1] + 1) not in basinunique:
								foundnew = True
								basinarea.append([basinpoint[0], basinpoint[1] + 1])
								basinunique.append("{},{}".format(basinpoint[0], basinpoint[1] + 1))

					#check down
			
					if basinpoint[0] < len(floormap) - 1:
						if floormap[basinpoint[0] + 1][basinpoint[1]] < 9:
							if "{},{}".format(basinpoint[0] + 1, basinpoint[1]) not in basinunique:
								foundnew = True
								basinarea.append([basinpoint[0] + 1, basinpoint[1]])
								basinunique.append("{},{}".format(basinpoint[0] + 1, basinpoint[1]))
			
					#check left

					if basinpoint[1] > 0:
						if floormap[basinpoint[0]][basinpoint[1] - 1] < 9:
							if "{},{}".format(basinpoint[0], basinpoint[1] - 1) not in basinunique:
								foundnew = True
								basinarea.append([basinpoint[0], basinpoint[1] - 1])
								basinunique.append("{},{}".format(basinpoint[0], basinpoint[1] - 1))
					
				
				print(basinarea)
				
			
			largestbasins.append(len(basinarea))


	print("Part 1: High points: {}".format(risk))			
		
	largestbasins.sort(reverse=True)
	
	print("Part 2: Basins: {}".format(largestbasins[0] * largestbasins[1] * largestbasins[2]))	
	
	exit()
	
'''
