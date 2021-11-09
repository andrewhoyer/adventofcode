inputdata = open("input-data.txt", "r").read()

# The number of values on each ticket. Set to 3 if using the sample test data.
numberofticketvalues = 20

# Break each section of the puzzle data into an array
sections = inputdata.split("\n\n")

# An array that will eventually hold dictionaries showing the name of each column.
# In each element, set an empty dictionary.
checks = []

for i in range(0,numberofticketvalues):
	checks.append({})

# Collect all of the rules, along with the name of the fields.
rules = []

for ticket in sections[0].split("\n"):
		
	rules.append({'name': ticket.split(": ")[0], 'rules': [[int(ticket.split(": ")[1].split(" or ")[0].split("-")[0]), int(ticket.split(": ")[1].split(" or ")[0].split("-")[1])], [int(ticket.split(": ")[1].split(" or ")[1].split("-")[0]), int(ticket.split(": ")[1].split(" or ")[1].split("-")[1])]]})


	for i in range(0,numberofticketvalues):
		checks[i][ticket.split(": ")[0]] = 1

# Get data for your own ticket

ignoredfirstline = False
ownticket = []

for ticket in sections[1].split("\n"):

	if ignoredfirstline == False:
		ignoredfirstline = True
		continue

	for ticketvalue in ticket.split(","):
		ownticket.append(int(ticketvalue))
	

# Process all nearby tickets

ignoredfirstline = False

goodtickets = []

for ticket in sections[2].split("\n"):
	
	if ignoredfirstline == False:
		ignoredfirstline = True
		continue

	if ticket == '':
		continue

	# Loop through every ticket element, looking for only valid tickets.
	validticket = False
	for ticketvalue in ticket.split(","):
		for rule in rules:
			if (int(ticketvalue) >= rule['rules'][0][0] and int(ticketvalue) <= rule['rules'][0][1]) or (int(ticketvalue) >= rule['rules'][1][0] and int(ticketvalue) <= rule['rules'][1][1]):
				validticket = True
				break
				
			else:
				validticket = False
				
		if validticket == False:
			break
	
	# For each valid ticket, remove dictionary elements which it doesn't match
	# The goal here is to reduce some of them down to one element, at which
	# point that can be used to start filtering out others.	

	if validticket == True:
		
		valuecounter = 0
		for ticketvalue in ticket.split(","):
			for rule in rules:
				if (int(ticketvalue) >= rule['rules'][0][0] and int(ticketvalue) <= rule['rules'][0][1]) or (int(ticketvalue) >= rule['rules'][1][0] and int(ticketvalue) <= rule['rules'][1][1]):
					continue
				else:
					# Remove the dictionary element if it doesn't match the rule.
					if rule['name'] in checks[valuecounter]:
						checks[valuecounter].pop(rule['name'])

			valuecounter = valuecounter + 1
				
		goodtickets.append(ticket)


# Loop through the checks array, locating dictionaries with only one item. Those being
# treated as unique, are removed from all other dictionaries. Repeat until all 
# dictionaries have only one item.

allsingleelements = False

while (allsingleelements == False):

	singles = []

	for thischeck in checks:
		
		mykeys = list(thischeck.keys())
		
		if len(mykeys) == 1:
			singles.append(mykeys[0])
			
	
	# Exit the loop if every dictionary has one element.	
	if len(singles) == len(checks):
		allsingleelements = True
	else:
		for single in singles:
			for thischeck in checks:
				if len(thischeck.keys()) > 1 and single in thischeck:
					thischeck.pop(single)

# Lastly, multiply the values of "departure" ticket values in your own ticket.

puzzlevalue = 1
valuecounter = 0

for thischeck in checks:
	
	if "departure" in list(thischeck.keys())[0]:
		puzzlevalue = puzzlevalue * ownticket[valuecounter]
		
	valuecounter = valuecounter + 1

print(puzzlevalue)






