lines = open("input-data.txt", "r").readlines()

validpasswords = 0

for line in lines:
	
	values = line.split(' ')
	
	minmax = values[0].split('-')
	
	keycharacter = values[1].replace(':', '')
	
	password = [char for char in values[2].strip()]
	matches = 0
	
	if password[int(minmax[0]) - 1] == keycharacter:
		matches = matches + 1
		
	if password[int(minmax[1]) - 1] == keycharacter:
		matches = matches + 1
	
	if matches == 1:
		validpasswords = validpasswords + 1

print("Number of valid passwords: {}".format(validpasswords))
