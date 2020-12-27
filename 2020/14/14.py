import re

inputdata = open("input-data.txt", "r").readlines()

mask = ''
maskcharacters = []
values = {}

for input in inputdata:
	
	action = re.search(r'([a-zA-Z]+)', input.strip()).group()
	
	if action == 'mask':
		
		mask = input.strip().split(' = ')[1]
		maskcharacters = [char for char in mask]
		
	else:
		
		process = input.strip().split(' = ')
		
		memid = int(re.search(r'([0-9]+)', process[0]).group())
		
		memvalue = int(process[1])
		
		binary = [char for char in bin(memvalue).replace('0b', '')]
		
		for i in range(0, len(maskcharacters) - len(binary)):
			binary.insert(0, '0')
		
		for i in range(0, len(maskcharacters)):
			if maskcharacters[i] == 'X':
				pass
			else:
				binary[i] = maskcharacters[i]
				
		values[memid] = int("".join(binary), 2)
		
total = 0
for key in values.values():
		total = total + key
		
print("\nSum of values after mask processing: {}".format(total))
