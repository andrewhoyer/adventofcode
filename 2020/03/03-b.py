lines = open("input-data.txt", "r").readlines()

rows = []

columncount = 0

for line in lines:
	
	# Create a list of lists, by breaking down each line into characters
	rows.append([char for char in line.strip()])
	
	columncount = len(line.strip())

max_y = len(rows) - 1

# Paths to test. x,y
paths = [[1,1],[3,1],[5,1],[7,1],[1,2]]

answer = 1 #default, not zero which would result in a 0 result

for path in paths:

	x = 0
	y = 0

	treecount = 0

	while y < max_y:

		x = x + path[0] 
		y = y + path[1]
	
		if x > columncount - 1:
			x = x - columncount
	
		if rows[y][x] == '#':

			treecount = treecount + 1
	
	answer = answer * treecount

print("Answer: {}".format(answer))
