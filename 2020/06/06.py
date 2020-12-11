inputdata = open("input-data.txt", "r").read()

declarations = inputdata.split('\n\n')

totalquestionsanswered = 0

for declaration in declarations:
	
	# Important placement, as questions are for the group, not the individual
	questions = {}
	
	for individual in declaration.split():

		for question in [char for char in individual.strip()]:
			questions[question] = 1
		
	totalquestionsanswered = totalquestionsanswered + len(questions)	
		
print("Number of questions answered: {}".format(totalquestionsanswered))
