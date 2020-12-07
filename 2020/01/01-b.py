inputdata = open("input-data.txt", "r")
numbers = inputdata.readlines()

complete = False
first = 0
second = 0
third = 0
while complete == False:

	for firstnumber in numbers:
		for secondnumber in numbers:
			if firstnumber != secondnumber:
				for thirdnumber in numbers:
					if thirdnumber != firstnumber and thirdnumber != secondnumber:
						if int(firstnumber.strip()) + int(secondnumber.strip()) + int(thirdnumber.strip()) == 2020:
							first = int(firstnumber.strip())
							second = int(secondnumber.strip())
							third = int(thirdnumber.strip())
							complete = True
					if complete == True:
						break
			if complete == True:
				break
		if complete == True:
			break

print("{} * {} * {} = {}".format(first, second, third, first * second * third))
