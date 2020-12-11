inputdata = open("input-data.txt", "r").read()

declarations = inputdata.split('\n\n')

totalquestionsanswered = 0

for declaration in declarations:
	
	individualcount = 0
	
	# Important placement, as questions are for the group, not the individual
	questions = {}
	
	for individual in declaration.split():
		
		individualcount = individualcount + 1

		for question in [char for char in individual.strip()]:
			# Check if question has been answered already
			if question in questions.keys():
				questions[question] = questions[question] + 1
			else:
				questions[question] = 1
		
	# Questions count to total if they equal the number of individuals in the group
	for question in questions.keys():
		if questions[question] == individualcount:
			totalquestionsanswered = totalquestionsanswered + 1
		
print("Number of questions answered: {}".format(totalquestionsanswered))
