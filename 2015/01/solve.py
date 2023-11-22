import sys

argv1 = sys.argv[1] # Filename of puzzle data passed as parameter

inputdata = open(argv1, "r").read().strip()

floor                       = 0
position_first_at_basement  = 0
counter                     = 1

for ch in inputdata:
    if ch == '(':
        floor = floor + 1
    else:
        floor = floor - 1

    # For Part 2, watch for the first time the floor goes below 0    
    if floor == -1 and position_first_at_basement == 0:
       position_first_at_basement = counter
    
    counter = counter + 1
    
print("Part 1: Final floor: {}".format(floor))
print("Part 2: First time in basement: {}".format(position_first_at_basement))
