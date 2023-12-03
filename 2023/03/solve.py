import sys

argv1 = sys.argv[1] # Filename of puzzle data passed as parameter

inputdata = open(argv1, "r").readlines()

def solve():

    # Place the entire data file into an array of arrays
    grid = []

    for line in inputdata:
        line = line.strip()
        row = []

        for ch in line:
            row.append(ch)

        grid.append(row)

    sum_part1 = 0
    sum_part2 = 0

    gears = {} # Part 2

    for row in range(len(grid)):
        
        num_index_start     = 0
        num_index_end       = 0
        number_str          = ""
        is_finding_number   = False

        for column in range(len(grid[row])):

            should_check = False

            if grid[row][column].isdecimal():
                # Anytime a number is found, it must be added to the string,
                # and a flag set if it is a new number.
                number_str += grid[row][column]
                if is_finding_number == False:
                    num_index_start     = column
                    num_index_end       = column # Critical for single-digit numbers
                    is_finding_number  = True
                else:
                    num_index_end = column
            else:
                # If the current grid location is anything besides a number, and
                # a number is being found, the complete number is now ready and
                # a grid search can be started.
                if is_finding_number == True:
                    should_check = True

            # A special case for numbers at the end of a row
            if column >= len(grid[row]) - 1:
                if is_finding_number == True:
                    should_check = True    

            # If any of the above conditions indicate a complete number has been
            # found, begin the search of the surrounding grid.
            if should_check == True:
                
                is_finding_number = False                

                is_a_part_number = False
                for y in range(row - 1, row + 2):
                    
                    # Avoids out of bounds searches
                    if y < 0 or y > len(grid) - 1:
                        continue                        
                    for x in range(num_index_start - 1, num_index_end + 2):
                        
                        # Avoids out of bounds searches
                        if x > len(grid[y]) - 1:
                            continue

                        if grid[y][x] == '.' or grid[y][x].isdecimal() == True:
                            pass
                        else:
                            # Matches a character string
                            is_a_part_number = True
                        
                        # Part 2. Looks for the * character and builds a dictionary
                        # of coordinates and the number of parts for each one.
                        if grid[y][x] == '*':
                            if str(y) + ',' + str(x) in gears:
                                gears[str(y) + ',' + str(x)].append(int(number_str))
                            else:
                                gears[str(y) + ',' + str(x)] = [int(number_str)]  
                
                # Part 1
                if is_a_part_number == True: 
                    sum_part1 += int(number_str)
                
                # Clear the number string after checking the grid.
                number_str = ""
    
    # Part 2. Looks for all gears with only two elements.
    for gear in gears:
        if len(gears[gear]) == 2:
            sum_part2 += (gears[gear][0] * gears[gear][1])

    print(f"Answer for Part 1: {sum_part1}")
    print(f"Answer for Part 2: {sum_part2}")

solve()