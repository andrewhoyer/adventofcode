import sys
import pprint
pp = pprint.PrettyPrinter(indent=2)

argv1 = sys.argv[1] # Filename of puzzle data passed as parameter

inputdata = open(argv1, "r").readlines()

# Store the entire grid in an array
grid = [] 

for line in inputdata:
    row = []

    for ch in line.strip():
        row.append(ch)
    
    grid.append(row)


# Takes an entry point on the grid and a direction, and calculates
# the number of energized spaces
#
# entry_x and entry_y are the entry grid coordinates. Note that
# the function handles the adjustment of the starting position so
# that the first movement and square to be entergized is the 
# entry point specified.
#
# direction is "N", "E", "S", or "W"

def find_energized_spaces(entry_x, entry_y, direction):

    if direction == "N":
        entry_y += 1
    elif direction == "S":
        entry_y -= 1
    elif direction == "E":
        entry_x -= 1
    elif direction == "W":
        entry_x += 1

    beams = [
        {
            'x': entry_x,
            'y': entry_y,
            'dir': direction,
            'active': True,
            'last_energize': 0
        }
    ]

    beams_new = [] # Stores new beams which are added at the end of each iteration
    energized = {} # Logs which grid elements are energized

    should_end_loop = False
    energized_temp  = 0 # To compare last iteration's energized count to the current
    loop_counter    = 0 # To check the time for when squares stop being energized
    step_counter    = 0 # An iteration counter for checking beams that have no more to do

    while should_end_loop == False:
        
        for beam in range(0, len(beams)):
            
            # At each point, check N, S, W, and E, looking only for pipe connections
            # that can possibly connect to the current pipe.

            found_direction = False

            if beams[beam]['dir'] == "N":
                if beams[beam]['y'] == 0:
                    beams[beam]['active'] = False
                    continue
                
                beams[beam]['y'] -= 1

                if grid[beams[beam]['y']][beams[beam]['x']] in [".", "|"]:
                    pass
                elif grid[beams[beam]['y']][beams[beam]['x']] in ["-"]:
                    beams[beam]['dir'] = 'W'
                    new_beam = {
                            'x': beams[beam]['x'],
                            'y': beams[beam]['y'],
                            'dir': 'E',
                            'active': True,
                            'last_energize': 0
                        }

                    if new_beam not in beams:
                        beams_new.append(new_beam)
                    
                elif grid[beams[beam]['y']][beams[beam]['x']] in ["/"]:
                    beams[beam]['dir'] = "E"
                elif grid[beams[beam]['y']][beams[beam]['x']] in ["\\"]:
                    beams[beam]['dir'] = "W"

                # Refresh the beam if it's energized something.
                if f"{beams[beam]['x']},{beams[beam]['y']}" in energized:
                    pass
                else:
                    energized[f"{beams[beam]['x']},{beams[beam]['y']}"] = True
                    beams[beam]['last_energize'] = step_counter

                # Deactivate the beam if it's old enough and not energizing spaces
                if step_counter - beams[beam]['last_energize'] > 450:
                    beams[beam]['active'] = False

            if beams[beam]['dir'] == "S":
                if beams[beam]['y'] == len(grid) - 1:
                    beams[beam]['active'] = False
                    continue
                
                beams[beam]['y'] += 1

                if grid[beams[beam]['y']][beams[beam]['x']] in [".", "|"]:
                    pass
                elif grid[beams[beam]['y']][beams[beam]['x']] in ["-"]:
                    beams[beam]['dir'] = 'W'
                    new_beam = {
                            'x': beams[beam]['x'],
                            'y': beams[beam]['y'],
                            'dir': 'E',
                            'active': True,
                            'last_energize': 0
                        }

                    if new_beam not in beams:
                        beams_new.append(new_beam)
                    
                elif grid[beams[beam]['y']][beams[beam]['x']] in ["/"]:
                    beams[beam]['dir'] = "W"
                elif grid[beams[beam]['y']][beams[beam]['x']] in ["\\"]:
                    beams[beam]['dir'] = "E"

                # Refresh the beam if it's energized something.
                if f"{beams[beam]['x']},{beams[beam]['y']}" in energized:
                    pass
                else:
                    energized[f"{beams[beam]['x']},{beams[beam]['y']}"] = True
                    beams[beam]['last_energize'] = step_counter

                # Deactivate the beam if it's old enough and not energizing spaces
                if step_counter - beams[beam]['last_energize'] > 450:
                    beams[beam]['active'] = False

            if beams[beam]['dir'] == "W":
                if beams[beam]['x'] == 0:
                    beams[beam]['active'] = False
                    continue
                
                beams[beam]['x'] -= 1

                if grid[beams[beam]['y']][beams[beam]['x']] in [".", "-"]:
                    pass
                elif grid[beams[beam]['y']][beams[beam]['x']] in ["|"]:
                    beams[beam]['dir'] = 'N'
                    new_beam = {
                        'x': beams[beam]['x'],
                        'y': beams[beam]['y'],
                        'dir': 'S',
                        'active': True,
                        'last_energize': 0
                    }

                    if new_beam not in beams:
                        beams_new.append(new_beam)
                    
                elif grid[beams[beam]['y']][beams[beam]['x']] in ["/"]:
                    beams[beam]['dir'] = "S"
                elif grid[beams[beam]['y']][beams[beam]['x']] in ["\\"]:
                    beams[beam]['dir'] = "N"

                # Refresh the beam if it's energized something.
                if f"{beams[beam]['x']},{beams[beam]['y']}" in energized:
                    pass
                else:
                    energized[f"{beams[beam]['x']},{beams[beam]['y']}"] = True
                    beams[beam]['last_energize'] = step_counter

                # Deactivate the beam if it's old enough and not energizing spaces
                if step_counter - beams[beam]['last_energize'] > 450:
                    beams[beam]['active'] = False

            if beams[beam]['dir'] == "E":
                if beams[beam]['x'] == len(grid[0]) - 1:
                    beams[beam]['active'] = False
                    continue
                
                beams[beam]['x'] += 1

                if grid[beams[beam]['y']][beams[beam]['x']] in [".", "-"]:
                    pass
                elif grid[beams[beam]['y']][beams[beam]['x']] in ["|"]:
                    beams[beam]['dir'] = 'N'
                    new_beam = {
                        'x': beams[beam]['x'],
                        'y': beams[beam]['y'],
                        'dir': 'S',
                        'active': True,
                        'last_energize': 0
                    }

                    if new_beam not in beams:
                        beams_new.append(new_beam)

                elif grid[beams[beam]['y']][beams[beam]['x']] in ["/"]:
                    beams[beam]['dir'] = "N"
                elif grid[beams[beam]['y']][beams[beam]['x']] in ["\\"]:
                    beams[beam]['dir'] = "S"

                # Refresh the beam if it's energized something.
                if f"{beams[beam]['x']},{beams[beam]['y']}" in energized:
                    pass
                else:
                    energized[f"{beams[beam]['x']},{beams[beam]['y']}"] = True
                    beams[beam]['last_energize'] = step_counter
                
                # Deactivate the beam if it's old enough and not energizing spaces
                if step_counter - beams[beam]['last_energize'] > 450:
                    beams[beam]['active'] = False
            
        step_counter += 1
        loop_counter += 1

        # Checks to see if anything new has been energized
        if energized_temp < len(energized):
            energized_temp = len(energized)
            loop_counter = 0

        # If after roughly 5% of the total iterations passes with no updates, exit
        if loop_counter > 15:
            should_end_loop = True

        # Add any newly created beams to the main group
        beams = beams + beams_new
        beams_new = []     

        # Remove any inactive beams
        for beam in range(len(beams) - 1, 0, -1):
            if beams[beam]['active'] == False:
                beams.pop(beam)
    
    return len(energized)

# Part 1: Uses entry point 0,0 from the East.
print(f"Part 1 - Energized spaces: {find_energized_spaces(0,0,'E')}")

# Part 2: Find the beam configuration (entry point, from any direction on the grid)
# that energizes the greatest number of spaces

entries = []

for i in range(0, len(grid[0])):
    # Check entries from the North
    entries.append(find_energized_spaces(i, 0, "S"))

    # Check entries from the South
    entries.append(find_energized_spaces(i, len(grid) - 1, "N"))

for i in range(0, len(grid)):

    # Check entries from the East
    entries.append(find_energized_spaces(0, i, "E"))
    
    # Check entries from the West
    entries.append(find_energized_spaces(0, len(grid[0]) - 1, "W"))

entries.sort()
print(f"Part 2 - Most energized spaces: {entries[-1]}")

exit()
