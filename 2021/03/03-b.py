inputdata = open("input-data.txt", "r").readlines()

columns_one = [0,0,0,0,0,0,0,0,0,0,0,0]
columns_zero = [0,0,0,0,0,0,0,0,0,0,0,0]

oxygen = []
co2 = []

def recalculateColumns(array, columns_one, columns_zero):

	columns_one = [0,0,0,0,0,0,0,0,0,0,0,0]
	columns_zero = [0,0,0,0,0,0,0,0,0,0,0,0]

	for row in array:
		thiscounter = 0
		for item in row:
		
			if item == '0':
				columns_zero[thiscounter] += 1
			elif item == '1':
				columns_one[thiscounter] += 1	
	
			thiscounter += 1

	return columns_one, columns_zero


def oxyStartsWith(string):
  if string.startswith(oxygen_str):
    return True
  else:
    return False
    
def co2StartsWith(string):
  if string.startswith(co2_str):
    return True
  else:
    return False


for row in inputdata:

	oxygen.append(row.strip())
	co2.append(row.strip())	
	
	chars = list(row.strip())
	
	counter = 0
	
	for character in chars:
		
		if character == '0':
			columns_zero[counter] += 1
		elif character == '1':
			columns_one[counter] += 1	
				
		counter += 1

oxygen_str = ""
co2_str = ""
    
while len(oxygen) > 1:
		
	counter = 0

	while counter < 12:
		
		if columns_zero[counter] > columns_one[counter]:
			oxygen_str += "0"
		else:
			oxygen_str += "1"

		counter += 1
		
		oxygen = list(filter(oxyStartsWith, oxygen))
		
		if len(oxygen) == 1:
			break
		
		columns_one, columns_zero = recalculateColumns(oxygen, columns_one, columns_zero)
			
while len(co2) > 1:
		
	counter = 0

	while counter < 12:
	
		if columns_zero[counter] <= columns_one[counter]:
			co2_str += "0"
		else:
			co2_str += "1"

		counter += 1
				
		co2 = list(filter(co2StartsWith, co2))

		
		if len(co2) == 1:
			break

		columns_one, columns_zero = recalculateColumns(co2, columns_one, columns_zero)

print("oxygen: {}, co2: {}, oxygen * co2: {}".format(int(oxygen[0], 2), int(co2[0], 2), int(oxygen[0], 2) * int(co2[0], 2)) )
