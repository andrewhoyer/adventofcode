
def calculate(equation):

	print("calculating: {}".format(equation))
	
	mathtype = ""
	mathnumber = 0
	total = 0
	eqposition = 0
	
	while eqposition < len(equation):
	
		nextitem = equation[eqposition:eqposition+1]

		print("nextitem: {}".format(nextitem))
		
		if nextitem == "*" or nextitem == "+":
			mathtype = nextitem
			
			eqposition += 1
			
		elif nextitem == "(":
		
			# Parenthesis!
			
			parenthesis = 1
			eqposition += 1
			startingpoint = eqposition
			
			while parenthesis > 0:
				if equation[eqposition:eqposition+1] == ")":
					parenthesis -= 1
					
				if equation[eqposition:eqposition+1] == "(":
					parenthesis += 1
					
				eqposition += 1
				
			mathnumber = calculate(equation[startingpoint:eqposition - 1])
			
			if mathtype == "":
				total = mathnumber			
			else:
				if mathtype == "*":
					total = total * mathnumber
					
				if mathtype == "+":
					total = total + mathnumber

		else:
		
			# Number
			if mathtype == "":
				# First value
				total = int(nextitem)
			
			else:			
				mathnumber = int(nextitem)	
				
				if mathtype == "*":
					total = total * mathnumber
					
				if mathtype == "+":
					total = total + mathnumber
		
		
			eqposition += 1
		

	
	print("returning {}".format(total))
	return total

def bracketsforadditon(equation):
	
	eqposition = 0
	newequation = ""
	insidebrackets = False
	mathnumber = ""
	parenthesis = 0
	
	while eqposition < len(equation):
	
		nextitem = equation[eqposition:eqposition+1]
		
		if nextitem == "+":
			
			if insidebrackets == True:
				newequation += nextitem
			else:
				newequation
			
			mathtype = nextitem
			
			eqposition += 1
			
		else:
			
			if insidebrackets == True:
			
				if nextitem == ")":
					parenthesis -= 1
					newequation += nextitem
					
				elif nextitem == "(":
					parenthesis += 1
					newequation += nextitem
					
				elif nextitem == "*"
					newequation += nextitem
		
			


inputdata = open("input-data.txt", "r").readlines()

grandtotal = 0

for line in inputdata:

	print(brakcetsforaddition(line.strip().replace(" ", "")))	
	#linetotal = calculate(line.strip().replace(" ", ""))
	
	#print("{} : {}".format(line.strip(), linetotal))
	
	#grandtotal += linetotal
	
	

print("Sub of all calculated lines: {}".format(grandtotal))
