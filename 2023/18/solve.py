import sys
import pprint
import math 
pp = pprint.PrettyPrinter(indent=2)

argv1 = sys.argv[1] # Filename of puzzle data passed as parameter

inputdata = open(argv1, "r").readlines()

trench_coords = [{
    'x': 0,
    'y': 0,
    'color': '#ffffff'
}]

trench_log = {}

min_x = 0
max_x = 0
min_y = 0
max_y = 0

# Build the grid and log the location of "S"
count_move = 0
for line in inputdata:
    directions = line.strip().split(" ")

    if directions[0] == 'U':
        for y in range(trench_coords[-1]['y'] + 1, trench_coords[-1]['y'] + int(directions[1]) + 1):
            trench_coords.append({
                'x': trench_coords[-1]['x'],
                'y': y,
                'color': directions[2].replace("(","").replace(")","")
            })

            trench_log[f"{trench_coords[-1]['x']},{y}"] = True

            if y > max_y:
                max_y = y 

            count_move += 1
            
    elif directions[0] == 'D':
        for y in range(trench_coords[-1]['y'] - 1, trench_coords[-1]['y'] - (int(directions[1]) + 1), -1):
            trench_coords.append({
                'x': trench_coords[-1]['x'],
                'y': y,
                'color': directions[2].replace("(","").replace(")","")
            })
            
            trench_log[f"{trench_coords[-1]['x']},{y}"] = True

            if y < min_y:
                min_y = y

            count_move += 1
                    
    elif directions[0] == 'L':
        for x in range(trench_coords[-1]['x'] - 1, trench_coords[-1]['x'] - (int(directions[1]) + 1), -1):
            trench_coords.append({
                'x': x,
                'y': trench_coords[-1]['y'],
                'color': directions[2].replace("(","").replace(")","")
            })
            
            trench_log[f"{x},{trench_coords[-1]['y']}"] = True

            if x < min_x:
                min_x = x

            count_move += 1

    elif directions[0] == 'R':
        for x in range(trench_coords[-1]['x'] + 1, trench_coords[-1]['x'] + int(directions[1]) + 1):
            trench_coords.append({
                'x': x,
                'y': trench_coords[-1]['y'],
                'color': directions[2].replace("(","").replace(")","")
            })
            
            trench_log[f"{x},{trench_coords[-1]['y']}"] = True

            if x > max_x:
                max_x = x

            count_move += 1


# Remove the first entry which was duplicated by the last entry.
trench_coords.pop(0)



# This function takes a point on the grid and compares it to every point
# along the pipe, calculating avalue between π and -π with the original
# point as the center. For points inside the shape, the considered lines
# will eventually make a complete circle. For points outside the shape,
# it may make a complete revolution, but will always come back to less
# than a full turn.

def check_radians(col, row, trench_coords):

    last_radians = -5
    crossed_boundary = 0

    start = 0
    end = len(trench_coords)
    by = 1

    # For this specific range, reverse the direction of angle checking
    # as it reports incorrectly otherwise due to math reasons.
    if col == 1 and row > 0:
        start = len(trench_coords) - 1
        end = 0
        by = -1
        crossed_boundary += 1

    for space in range(start, end, by):
        new_radians = math.atan2(trench_coords[space]['x'] - col, trench_coords[space]['y'] - row)
            
        # Anytime the angle moves between π and -π, log it.    
        if last_radians != -5:
            if new_radians - last_radians > 2.0:
                crossed_boundary += 1
            elif new_radians - last_radians < -2.0:
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

# File output for debugging. All file operations are commented out.
#output = open("output.txt", "a")

for row in range(max_y, min_y - 1, -1):
    line = ""

    last_block = ""
    check = False

    for col in range(min_x, max_x + 1):
        if f"{col},{row}" in trench_log:
            # Trench

            #if col == 0 and row == 0:
            #    line += "🟨"
            #else:
            #    line += "⬛️" #"#" #

            # Saves a lot of processing as it ignores everything until the first edge is reached
            last_block = "trench"

            # Trench already counted in len(trench_coords)
            continue 

        else:
            if last_block == "trench":
                check = check_radians(col, row, trench_coords)

                if check == True:
                    #line += "🟥"
                    last_block = "inner"
                else:
                    #line += "🟩"
                    last_block = "outer"
            elif last_block == "inner":
                #line += "🟥"
                check = True
            elif last_block == "outer":
                #line += "🟩"
                check = False
        
        if check == True:
            enclosed_space += 1
    
    #output.write(line + "\n")

#output.close()

print(f"Part 1 - Total area: {enclosed_space + len(trench_coords)}")

exit()
