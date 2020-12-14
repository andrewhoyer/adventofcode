import re

inputdata = open("input-data.txt", "r").readlines()

position     = 0
accumulator  = 0
testcounter  = 0
instructions = []
history      = [] # Tracks which instructions have been executed during a test
fixhistory   = [] # A list of jmp elements which have been changed to nop for testing
programcompleted = False


for input in inputdata:

	parts = input.strip().split(' ');

	number = int(re.search(r'(\d+)', parts[1]).group())
	direction = re.search(r'(\W{1})', parts[1]).group()
	
	if direction == '-':
		number = number * -1
		
	instructions.append([parts[0], number])

while True:

	instructions_test = instructions
	history           = []
	accumulator       = 0
	position          = 0
	
	testcounter = testcounter + 1
	updatedjmp  = False
	
	print("\nTest #{}".format(testcounter))

	while True:
	
		if position in history:
			print("Infinite loop, abort")
			break
		else:
		
			history.append(position)
		
			if instructions[position][0] == 'acc':
				accumulator = accumulator + instructions[position][1]
				position = position + 1

			elif instructions[position][0] == 'jmp':
			
				# Repair each jmp, but only one per test, and a different one each time
				if position not in fixhistory and updatedjmp == False:
					# Treat jmp as nop, set values, then move on to the next instruction
					print("Fixing jmp at position {}".format(position))
					fixhistory.append(position)
					updatedjmp = True
					position = position + 1
				else:
					position = position + instructions[position][1]

			elif instructions[position][0] == 'nop':
				position = position + 1
			
		if position >= len(instructions_test) - 1:
			print("Program completed!")
			programcompleted = True
	
		if programcompleted:
			break
			
	if programcompleted:
		break		
		
print("\nFinal Accumulator: {}".format(accumulator))
