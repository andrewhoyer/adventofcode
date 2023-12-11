import sys
import pprint
pp = pprint.PrettyPrinter(indent=2)

argv1 = sys.argv[1] # Filename of puzzle data passed as parameter

inputdata = open(argv1, "r").readlines()

grid    = [] # Holds the entire grid in an array
start_x = 0  # Holds the starting position of the "S" element
start_y = 0

# Build the grid and log the location of "S"
count_row = 0
for line in inputdata:
    row = []

    count_col = 0
    for ch in line.strip():
        row.append(ch)

        if ch == "S":
            start_x = count_col
            start_y = count_row

        count_col += 1
    
    grid.append(row)

    count_row += 1

current_x       = start_x
current_y       = start_y
next_pipe       = ""
direction_from  = ""
steps           = 0

# Keep finding connecting pipes until "S" is reached, completing the loop.
while next_pipe != "S":

    # At each point, check N, S, W, and E, looking only for pipe connections
    # that can possibly connect to the current point.

    found_direction = False

    if direction_from != "N":
        if next_pipe in ["|", "J", "L", ""]:
            if current_y - 1 >= 0:
                if grid[current_y - 1][current_x] in ["|", "F", "7", "S"]:
                    current_y -= 1
                    next_pipe = grid[current_y][current_x]        
                    direction_from = "S"
                    found_direction = True
        
    if direction_from != "S" and found_direction == False:
        if next_pipe in ["|", "F", "7", ""]:
            if current_y + 1 <= len(grid) - 1:
                if str(grid[current_y + 1][current_x]) in ["|", "L", "J", "S"]:
                    current_y += 1
                    next_pipe = grid[current_y][current_x]
                    direction_from = "N"
                    found_direction = True
    
    if direction_from != "W" and found_direction == False:
        if next_pipe in ["-", "7", "J", ""]:
            if current_x - 1 >= 0:
                if grid[current_y][current_x - 1]  in ["-", "L", "F", "S"]:
                        current_x -= 1
                        next_pipe = grid[current_y][current_x]
                        direction_from = "E"
                        found_direction = True
                        
    if direction_from != "E" and found_direction == False:
        if next_pipe in ["-", "F", "L", ""]:
            if current_x + 1 <= len(grid[current_y]) - 1:
                if grid[current_y][current_x + 1] in ["-", "7", "J", "S"]:
                        current_x += 1
                        next_pipe = grid[current_y][current_x]
                        direction_from = "W"
                        found_direction = True

    steps += 1

print(f"Part 1 - Steps to furthest distance from 'S': {steps // 2}")

exit()
