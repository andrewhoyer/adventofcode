inputdata = open("puzzle-input.txt", "r").read()

# Part 1

char_array = []
counter    = 1

for char in inputdata.strip():
	char_array.append(char)

	if len(char_array) > 4:
		char_array.pop(0)
		
		test_set = set()
		for item in char_array:
			test_set.add(item)
			
		if len(test_set) == 4:
			print("start-of-packet marker after character: {}".format(counter))
			break;

	counter = counter + 1

# Part 2

char_array = []
counter    = 1

for char in inputdata.strip():
	char_array.append(char)

	if len(char_array) > 14:
		char_array.pop(0)
		
		test_set = set()
		for item in char_array:
			test_set.add(item)
			
		if len(test_set) == 14:
			print("start-of-message marker after character: {}".format(counter))
			break;
	
	counter = counter + 1		

exit()
