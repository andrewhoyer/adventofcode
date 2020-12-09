inputdata = open("input-data.txt", "r").read()

passports = inputdata.split('\n\n')

validpassports = 0
elementsrequired = 7

for passport in passports:
	elements = passport.split()
	
	elementsfound = 0
	
	dict = {}
	
	for element in elements:
		elementparts = element.split(':')
		
		if elementparts[0] == 'byr':
			dict[elementparts[0]] = 1
		elif elementparts[0] == 'iyr':
			dict[elementparts[0]] = 1
		elif elementparts[0] == 'eyr':
			dict[elementparts[0]] = 1
		elif elementparts[0] == 'hgt':
			dict[elementparts[0]] = 1
		elif elementparts[0] == 'hcl':
			dict[elementparts[0]] = 1
		elif elementparts[0] == 'ecl':
			dict[elementparts[0]] = 1
		elif elementparts[0] == 'pid':
			dict[elementparts[0]] = 1
		
	if len(dict) == elementsrequired:
		validpassports = validpassports + 1
	else:
		print(dict)
			
print("Number of valid passports: {}".format(validpassports))
