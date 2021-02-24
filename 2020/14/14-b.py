import re
import copy

inputdata = open("input-data.txt", "r").readlines()

mask           = ''
maskcharacters = []
values         = {}

def setvaluesformemoryaddresses(binaryarray, startingindex, memvalue, depth):

	# Indenting really helps with debugging, to show search depth level
	spaces = ''
	for _ in range(depth):
		spaces = spaces + '  '		
	
	if startingindex > len(binaryarray) - 1:
		values[int("".join(binaryarray), 2)] = memvalue	
	else:
		if binaryarray[startingindex] == 'X':
			# Where the value is X, start recursion using a 0 and 1
			for i in range(0,2):
				binarycopy = copy.deepcopy(binaryarray)
				binarycopy[startingindex] = str(i)
				setvaluesformemoryaddresses(binarycopy, startingindex + 1, memvalue, depth + 1)
		else:
			# For 0 and 1, just move one level deeper
			binarycopy = copy.deepcopy(binaryarray)
			setvaluesformemoryaddresses(binarycopy, startingindex + 1, memvalue, depth + 1)


for input in inputdata:
	
	action = re.search(r'([a-zA-Z]+)', input.strip()).group()
	
	if action == 'mask':
		
		mask = input.strip().split(' = ')[1]
		maskcharacters = [char for char in mask]
		
	else:
		
		process  = input.strip().split(' = ')
		memid    = int(re.search(r'([0-9]+)', process[0]).group())
		memvalue = int(process[1])
		binary   = [char for char in bin(memid).replace('0b', '')]

		# Create 36-character string by adding '0' padding
		for i in range(0, len(maskcharacters) - len(binary)):
			binary.insert(0, '0')
		
		# Masking rules		
		for i in range(0, len(maskcharacters)):
			if maskcharacters[i] == '0':
				pass
			elif maskcharacters[i] == '1':
				binary[i] = maskcharacters[i]
			else:
				binary[i] = 'X'
		
		# Pass the value to the recurring function for processing
		setvaluesformemoryaddresses(binary, 0, memvalue, 0)

		
total = 0
for value in values.values():
		total = total + value
		
print("\nSum of values after mask processing: {}".format(total))
