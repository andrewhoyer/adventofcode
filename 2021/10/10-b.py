if __name__ == "__main__":
	
	inputdata = open("input-data.txt", "r").readlines()
	
	#originaldata = inputdata.split(" | ")
	
	
	rowscores = []
	
	
	for row in inputdata:
		print("--------------")
		print(row)
		
		type_paren = 0
		type_square = 0
		type_curly = 0
		type_angle = 0
		
		syntaxarray = []
		
		corruptline = False
		
		for column in [char for char in row.strip()]:
			#print(column)
			if column == "(":
				syntaxarray.append(column)
				continue
				#type_paren += 1
				#print(type_paren)
				
			if column == "[":
				syntaxarray.append(column)	
				continue
				#type_square += 1
				#print(type_square)

			if column == "{":
				syntaxarray.append(column)
				continue
				#type_curly += 1
				#print(type_curly)
											
			if column == "<":
				syntaxarray.append(column)
				continue
				#type_angle += 1
				#print(type_angle)
			
			
			if column == ")":
				#type_paren -= 1
				#print(type_paren)
				
				#if type_paren < 0:
				if syntaxarray[-1] == "(":
					syntaxarray.pop()
				else:
					corruptline = True
					break
				
			if column == "]":
				
				if syntaxarray[-1] == "[":
					syntaxarray.pop()
				else:
					corruptline = True
					break

			if column == "}":
				if syntaxarray[-1] == "{":
					syntaxarray.pop()
				else:
					corruptline = True
					break
											
			if column == ">":
				if syntaxarray[-1] == "<":
					syntaxarray.pop()
				else:
					corruptline = True
					break
		
		
		
		if corruptline == False:
			
			print("incomplete line: {}".format(row.strip()))
			print(syntaxarray)
			
			rowscore = 0
			
			for i in range(len(syntaxarray) -1, -1, -1):
				#print(i)
				
				if syntaxarray[i] == "(":
					rowscore = rowscore * 5 + 1
					syntaxarray.pop()
				elif syntaxarray[i] == "[":
					rowscore = rowscore * 5 + 2
					syntaxarray.pop()
				elif syntaxarray[i] == "{":
					rowscore = rowscore * 5 + 3
					syntaxarray.pop()
				elif syntaxarray[i] == "<":
					rowscore = rowscore * 5 + 4
					syntaxarray.pop()
			
					
			rowscores.append(rowscore)
			
		
		"""
		syntaxscore += rowscore
		print("-----")
		print(rowscore)
		print(syntaxscore)
		print("=====")		
		"""
	print(len(sorted(rowscores)))
	print(int(len(rowscores) / 2))
	print(sorted(rowscores))	
	print(sorted(rowscores)[int(len(rowscores) / 2)])
			
			