lines = open("input-data.txt", "r").readlines()

validpasswords = 0

for line in lines:
	
	values = line.split(' ')
	
	minmax = values[0].split('-')
	
	keycharacter = values[1].replace(':', '')
	
	charcount = 0
	
	for char in values[2].strip():
		if char == keycharacter:
			charcount = charcount + 1
	
	if charcount >= int(minmax[0]) and charcount <= int(minmax[1]):
		validpasswords = validpasswords + 1

print("Number of valid passwords: {}".format(validpasswords))
