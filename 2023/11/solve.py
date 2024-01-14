import sys
import pprint
import math 
pp = pprint.PrettyPrinter(indent=2)

argv1 = sys.argv[1] # Filename of puzzle data passed as parameter

inputdata = open(argv1, "r").readlines()

grid    = [] # Holds the entire grid in an array\\

# Build the grid
for line in inputdata:
    row = []

    for ch in line.strip():
        row.append(ch)
    
    grid.append(row)

# Determine which rows are empty
empty_rows = []
for i in range(len(grid) - 1, 0, -1):
    
    empty_row = True
    for ch in grid[i]:
        if ch == "#":
            empty_row = False
            break
    
    if empty_row == True:
        empty_rows.append(i)

# Determine which columns are empty
empty_columns = []
for i in range(len(grid[0]) - 1, -1, -1):
    empty_col = True
    for j in range(len(grid) - 1, -1, -1):
        
        if len(grid[j]) == 0:
            continue

        if grid[j][i] == "#":
            empty_col = False
            break
        
    if empty_col == True:
        empty_columns.append(i)

# Determine locations of all galaxies
galaxies = []
for i in range(0, len(grid)):
    for j in range(0, len(grid[i])):
        if grid[i][j] == "#":
            galaxies.append([j, i])

def sum_distances(part):

    # Calculate sum of shortest distance between each galaxy.
    distance = 0

    # Expansion rate for part 1 and part 2
    expansion = 2
    if part == 2:
        expansion = 1000000

    # Loop through each galaxy
    for i in range(0, len(galaxies)):

        # Compare to every other galaxy (besides ones already searched)
        for j in range(i + 1, len(galaxies)):

            x1 = 0
            x2 = 0
            y1 = 0
            y2 = 0

            # Set up the values to compare and reverse them so
            # x1 and y1 is less than x2 and y2
            x1 = galaxies[i][0]
            x2 = galaxies[j][0]
            y1 = galaxies[i][1]
            y2 = galaxies[j][1]

            if galaxies[i][0] > galaxies[j][0]:
                x2 = galaxies[i][0]
                x1 = galaxies[j][0]

            if galaxies[i][1] > galaxies[j][1]:
                y2 = galaxies[i][1]
                y1 = galaxies[j][1]
            
            # Calculate horizontal difference between the two galaxies
            for k in range(x1, x2):
                
                # For each empty column, add the expansion, otherwise add 1
                if k in empty_columns:
                    distance += expansion
                else:
                    distance += 1
            
            # Calculate vertical difference between the two galaxies
            for k in range(y1, y2):
                
                # For each row column, add the expansion, otherwise add 1
                if k in empty_rows:
                    distance += expansion
                else:
                    distance += 1
                
    print(f"Part {part}, expansion rate {expansion}: Sum of the shortest distances between galaxies: {distance}")   

sum_distances(1)
sum_distances(2)

exit()
