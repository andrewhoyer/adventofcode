import sys
import pprint
import math 
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

# Part 2 - Used to store coordinates of all pipes
pipe_coords = []

# Keep finding connecting pipes until "S" is reached, completing the loop.
while next_pipe != "S":

    # At each point, check N, S, W, and E, looking only for pipe connections
    # that can possibly connect to the current pipe.

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

    pipe_coords.append([current_x, current_y])
    steps += 1

print(f"Part 1 - Steps to furthest distance from 'S': {steps // 2}")


# For Part 2
# This function takes a point on the grid and compares it to every point
# along the pipe, calculating avalue between π and -π with the original
# point as the center. For points inside the shape, the considered lines
# will eventually make a complete circle. For points outside the shape,
# it may make a complete revolution, but will always come back to less
# than a full turn.

def check_radians(col, row, pipe_coords):

    last_radians = -5
    crossed_boundary = 0
    
    for pipe in pipe_coords:
        
        new_radians = math.atan2(pipe[0] - col, pipe[1] - row)
        
        if last_radians != -5:
            
            # Anytime the angle moves between π and -π, log it.
            if new_radians - last_radians > 4.0:
                crossed_boundary += 1
            elif new_radians - last_radians < -4.0:
                crossed_boundary += 1

        last_radians = new_radians
    
    # The test! If the angles calculated complete a full turn, crossing
    # the π boundary, the result will be odd. Even results means the angle
    # calculations never made it a full turn (0), or eventually moved back.
    if crossed_boundary % 2 == 0:
       return False
    else:
        return True


# Consider every grid space except for the pipe itself, and determine whether
# or not it is inside or outside the shape.
enclosed_space = 0
for row in range(0, len(grid)):
    for col in range(0, len(grid[row])):
        if [col, row] in pipe_coords:
            pass
        else:
            if check_radians(col, row, pipe_coords) == True:
                enclosed_space += 1

print(f"Part 2 - The number of grid spaces encolsed by the pipe: {enclosed_space}")

exit()
