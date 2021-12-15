if __name__ == "__main__":
	
	inputdata = open("input-data.txt", "r").readlines()
	
	# Generate the floor map based on the puzzle data
	floormap = []
	
	for row in inputdata:
		
		rowarray = []
		heightarray = []
		for column in [char for char in row.strip()]:	
			
			rowarray.append(int(column))
			heightarray.append(0)
			
		floormap.append(rowarray)
	
	# Risk value for part 1
	risk = 0
	
	# Collection of the basin sizes for part 2
	largestbasins = []
			
	# Process the entire floor map	
	for rowindex, row in enumerate(floormap):
		for colindex, height in enumerate(row):
			
			# Check nearby locations, and only add the risk value if they're all lower
			
			#check up
			if rowindex > 0:
				if floormap[rowindex - 1][colindex] <= height:
					continue
							
			#check right
			if colindex < len(row) - 1:
				if floormap[rowindex][colindex + 1] <= height:
					continue
			
			#check down
			if rowindex < len(floormap) - 1:
				if floormap[rowindex + 1][colindex] <= height:
					continue
			
			#check left
			if colindex > 0:
				if floormap[rowindex][colindex - 1] <= height:
					continue
		
			# Found a low point at rowindex, colindex
			risk += (1 + height)	
			
			# For this low point, calculate the entire basin area surrounded by 9's

			# To store coordinates of the basin area
			basinarea = [[rowindex,colindex]]
			
			# A unique list for optimization
			basinunique = ["{},{}".format(rowindex, colindex)]
			
			# Starting from the low point, check up/down and left/right. If these are less
			# than 9, add them to the basin area, then repeat the process for those new
			# locations. Eventually, the entire available area is covered.
			
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
					
				
				#print(basinarea)
			
			# Add the the area of the basin to the array
			largestbasins.append(len(basinarea))


	print("Part 1: High points: {}".format(risk))			
	
	# For part 2, order the basins, then multiply the largest three.
	largestbasins.sort(reverse=True)
	
	print("Part 2: Basin area calculation: {}".format(largestbasins[0] * largestbasins[1] * largestbasins[2]))	
	
	exit()
	
