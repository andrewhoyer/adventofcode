inputdata = open("input-data.txt", "r").readlines()

columns_one = [0,0,0,0,0,0,0,0,0,0,0,0]
columns_zero = [0,0,0,0,0,0,0,0,0,0,0,0]

gamma = ""
epsilon = ""

for row in inputdata:
	
	chars = list(row.strip())
	print(chars)
	
	counter = 0
	zeroes = 0
	ones = 0
	
	for character in chars:
		
		if character == '0':
			columns_zero[counter] += 1
		elif character == '1':
			columns_one[counter] += 1	
		

					
		counter += 1
	
counter = 0

while counter < 12:
	
	if columns_zero[counter] > columns_one[counter]:
		gamma += "0"
		epsilon += "1"
	else:
		gamma += "1"
		epsilon += "0"

	counter += 1
	

print(columns_zero)
print(columns_one)

print(gamma)
print(epsilon)


print(int(gamma, 2))
print(int(epsilon, 2))

print(int(gamma, 2) * int(epsilon, 2))
#print("Horiz: {}, Depth: {}, Multiplied: {}".format(horizontal, depth, horizontal * depth))
