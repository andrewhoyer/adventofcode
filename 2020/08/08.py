import re

inputdata = open("input-data.txt", "r").readlines()

position = 0
accumulator = 0
instructions = []
history = []

for input in inputdata:

	parts = input.strip().split(' ');

	number = int(re.search(r'(\d+)', parts[1]).group())
	direction = re.search(r'(\W{1})', parts[1]).group()
	
	if direction == '-':
		number = number * -1
		
	instructions.append([parts[0], number])

while True:
	
	if position in history:
		break
	else:
		
		history.append(position)
		
		if instructions[position][0] == 'acc':
			accumulator = accumulator + instructions[position][1]
			position = position + 1

		elif instructions[position][0] == 'jmp':
			position = position + instructions[position][1]

		elif instructions[position][0] == 'nop':
			position = position + 1
			
		print("Accumulator: {}. Move position to: {}".format(accumulator, position))
		
print("\nFinal Accumulator: {}".format(accumulator))
