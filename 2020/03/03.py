lines = open("input-data.txt", "r").readlines()

rows = []

columncount = 0

for line in lines:
	
	# Create a list of lists, by breaking down each line into characters
	rows.append([char for char in line.strip()])
	
	columncount = len(line.strip())
	
x = 0
y = 0

max_y = len(rows) - 1

treecount = 0

while y < max_y:

	x = x + 3 
	y = y + 1
	
	if x > columncount - 1:
		x = x - columncount
	
	if rows[y][x] == '#': # Tree
		treecount = treecount + 1

print("Number of trees hit: {}".format(treecount))
