if __name__ == "__main__":
	
	inputdata = open("input-data.txt", "r").readlines()
	
	#originaldata = inputdata.split(" | ")
	
	
	syntaxscore = 0
	
	
	for row in inputdata:
		print("--------------")
		print(row)
		
		type_paren = 0
		type_square = 0
		type_curly = 0
		type_angle = 0
		
		syntaxarray = []
		
		rowscore = 0
		
		for column in [char for char in row.strip()]:
			print(column)
			if column == "(":
				syntaxarray.append(column)
				#type_paren += 1
				#print(type_paren)
				
			if column == "[":
				syntaxarray.append(column)	
				#type_square += 1
				#print(type_square)

			if column == "{":
				syntaxarray.append(column)
				#type_curly += 1
				#print(type_curly)
											
			if column == "<":
				syntaxarray.append(column)
				#type_angle += 1
				#print(type_angle)
			
			
			if column == ")":
				#type_paren -= 1
				#print(type_paren)
				
				#if type_paren < 0:
				if syntaxarray[-1] == "(":
					syntaxarray.pop()
				else:
					rowscore = 3
					break
				
			if column == "]":
				
				if syntaxarray[-1] == "[":
					syntaxarray.pop()
				else:
					rowscore = 57
					break

			if column == "}":
				if syntaxarray[-1] == "{":
					syntaxarray.pop()
				else:
					rowscore = 1197
					break
											
			if column == ">":
				if syntaxarray[-1] == "<":
					syntaxarray.pop()
				else:
					rowscore = 25137
					break
		
		
		syntaxscore += rowscore
		print("-----")
		print(rowscore)
		print(syntaxscore)
		print("=====")		
	
	print(syntaxscore)
			
			