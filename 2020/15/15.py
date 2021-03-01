inputdata    = [2,0,6,12,1,3]

spoken       = len(inputdata)
firstelement = 0;


while spoken < 2020:
	
	flag = False
	difference = 0

	for element in range(len(inputdata), 0, -1):
		
		if flag == False:
			firstelement = inputdata[element - 1]
			flag = True
		else:
			if firstelement == inputdata[element - 1]:
				difference = len(inputdata) - element
				break
				
	
	inputdata.append(difference)
	spoken = spoken + 1


		
print("Number {} spoken is: {}".format(spoken, inputdata[-1]))
