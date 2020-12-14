import re

inputdata = open("input-data.txt", "r").readlines()

bagdefinitions = {}
colortosearchfor = 'shiny gold'
bagsthatcontaincolor = 0

for input in inputdata:
	definition = re.split(r' bags contain \d ', input.strip())

	if len(definition) == 1:
		bagdefinitions[re.split(r' bags contain no other bags.', input.strip())[0]] = ''
	else:
		
		bagdescriptions = definition[1].replace(' bags.', '')
		bagdescriptions = bagdescriptions.replace(' bag.', '')		
		bagdescriptions = bagdescriptions.replace(' bags', '')
		bagdescriptions = bagdescriptions.replace(' bag', '')
	
		bagdefinitions[definition[0]] = re.split(r', \d ', bagdescriptions)


def checkbag(bagcolor, colortosearchfor, depth):
	"Checks a single bag for the color, then calls itself to look at deeper levels"
	
	# Indenting really helps with debugging, to show search depth level
	spaces = ''
	for _ in range(depth):
		spaces = spaces + '  '
	
	print("{}Checking bag {}: {}".format(spaces, bagcolor, bagdefinitions[bagcolor]))
	
	# Check for matching colors in this bag.
	if colortosearchfor in bagdefinitions[bagcolor]:
		print("{}* This bag contains the matching color!\n\n".format(spaces))
		return True
	
	for innerbag in bagdefinitions[bagcolor]:
	
		# Exit the function if a bag is found in a deeper level
		if checkbag(innerbag, colortosearchfor, depth + 1) == True:
			return True;

	# No matches are found in all inner bags
	return False


# Kick off the recursive function!

for bag in bagdefinitions.keys():
	if checkbag(bag, colortosearchfor, 0) == True:
		bagsthatcontaincolor = bagsthatcontaincolor + 1

print("Number of bags that can contain a {} bag: {}".format(colortosearchfor, bagsthatcontaincolor))
