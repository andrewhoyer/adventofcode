import re

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
			if re.match('\d{4}', elementparts[1]) and len(elementparts[1]) == 4 and int(elementparts[1]) >= 1920 and int(elementparts[1]) <= 2002:
				dict[elementparts[0]] = elementparts[1]

		elif elementparts[0] == 'iyr':
			if re.match('\d{4}', elementparts[1]) and len(elementparts[1]) == 4 and int(elementparts[1]) >= 2010 and int(elementparts[1]) <= 2020:
				dict[elementparts[0]] = elementparts[1]

		elif elementparts[0] == 'eyr':
			if re.match('\d{4}', elementparts[1]) and len(elementparts[1]) == 4 and int(elementparts[1]) >= 2020 and int(elementparts[1]) <= 2030:
				dict[elementparts[0]] = elementparts[1]

		elif elementparts[0] == 'hgt':
			if re.match(r'[0-9]*(in|cm)', elementparts[1]):
				height = int(re.search(r'[0-9]*', elementparts[1]).group(0))
				unit   = re.search(r'(in|cm)', elementparts[1]).group(0)
				
				if unit == 'cm':
					if height >= 150 and height <= 193:
						dict[elementparts[0]] = elementparts[1]		
				
				else:
					if height >= 59 and height <= 76:
						dict[elementparts[0]] = elementparts[1]		
				
		elif elementparts[0] == 'hcl':
			if re.match(r'#[0-9a-f]{6}', elementparts[1]) and len(elementparts[1]) == 7:
				dict[elementparts[0]] = elementparts[1]	
			
		elif elementparts[0] == 'ecl':
			if elementparts[1] == 'amb' or elementparts[1] == 'blu' or elementparts[1] == 'gry' or elementparts[1] == 'grn' or elementparts[1] == 'hzl' or elementparts[1] == 'oth' or elementparts[1] == 'brn':
				dict[elementparts[0]] = elementparts[1]

		elif elementparts[0] == 'pid':
			if re.match(r'[0-9]{9}', elementparts[1]) and len(elementparts[1]) == 9:
				dict[elementparts[0]] = elementparts[1]	

		
	if len(dict) == elementsrequired:
		validpassports = validpassports + 1
			
print("Number of valid passports: {}".format(validpassports))
