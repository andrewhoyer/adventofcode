inputdata = open("input-data.txt", "r").read()

sections = inputdata.split("\n\n")

rules = []
for line in sections[0].split("\n"):
	rules.append([[int(line.split(": ")[1].split(" or ")[0].split("-")[0]), int(line.split(": ")[1].split(" or ")[0].split("-")[1])], [int(line.split(": ")[1].split(" or ")[1].split("-")[0]), int(line.split(": ")[1].split(" or ")[1].split("-")[1])]])

ignoredfirstline = False
invalidtotal = 0

for line in sections[2].split("\n"):
	if ignoredfirstline == False:
		ignoredfirstline = True
		continue

	if line == '':
		continue

	for ticketvalue in line.split(","):
		valuematch = False

		for rule in rules:
			if (int(ticketvalue) >= rule[0][0] and int(ticketvalue) <= rule[0][1]) or (int(ticketvalue) >= rule[1][0] and int(ticketvalue) <= rule[1][1]):
				valuematch = True
				break
		
		if valuematch == False:
			invalidtotal = invalidtotal + int(ticketvalue)
		
print("Total of invalid values: {}".format(invalidtotal))

