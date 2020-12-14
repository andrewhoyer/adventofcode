import re

inputdata = open("input-data.txt", "r").readlines()

bagdefinitions = {}
colortosearchfor = 'shiny gold'

for input in inputdata:
	definition = re.split(r' bags contain ', input.strip())

	if definition[1] == 'no other bags.':
		bagdefinitions[re.split(r' bags contain no other bags.', input.strip())[0]] = []
	else:
		
		bagdescriptions = definition[1].replace(' bags.', '')
		bagdescriptions = bagdescriptions.replace(' bag.', '')		
		bagdescriptions = bagdescriptions.replace(' bags', '')
		bagdescriptions = bagdescriptions.replace(' bag', '')
	
		innerbags = []
	
		for thisbag in bagdescriptions.split(', '):
			thisbagdef = thisbag.split(' ', 1)
			innerbags.append({thisbagdef[1]: int(thisbagdef[0])})
	
		bagdefinitions[definition[0]] = innerbags

def numberofbagsinthisbag(bagcolor, depth):
	"Returns the number of bags contained in this bag, then calls itself to check for bags within those bags"
	
	numbags = 0
	
	# Indenting really helps with debugging, to show search depth level
	spaces = ''
	for _ in range(depth):
		spaces = spaces + '   '
	
	print("\n{}Checking bag {}: {}".format(spaces, bagcolor, bagdefinitions[bagcolor]))
	
	# Count bags in this bagg
	for innerbagcolor in bagdefinitions[bagcolor]:
		for color in innerbagcolor.keys():

			numbags = numbags + innerbagcolor[color]
			
			# Recursive call. Important: Must multiply the return value by the number of bags specified on this level!
			numbags = numbags + numberofbagsinthisbag(color, depth + 1) * innerbagcolor[color]

	return numbags


# Kick off the recursive function!
bagscontainedincolor = numberofbagsinthisbag(colortosearchfor, 0)

print("Number of bags that are contained in a {} bag: {}".format(colortosearchfor, bagscontainedincolor))
