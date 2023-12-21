import sys
import pprint

pp = pprint.PrettyPrinter(indent=2)

argv1 = sys.argv[1] # Filename of puzzle data passed as parameter

inputdata = open(argv1, "r").readlines()


# Evaluates whether a suggested combination is a match for the allowed pattern
def evaluate_combination(pattern, combination, spaces_indent):

    for i in range(0, len(combination)):

        # A part in a combination must match one of these in the pattern
        if combination[i] == "#":
            if pattern[i] in ["#", "?"]:
                pass
            else:
                return False
        # Ensure that a part exists where it's a necessary match in the pattern
        if pattern[i] == "#" and combination[i] != "#":
            return False
        
    return True


# A recursive function that considers the first and last items in the list,
# and handles the middle parts lists separately.
def get_combinations(pattern, combination, groups, spaces, depth):
    
	# Indenting really helps with debugging, to show search depth level
    spaces_indent = ''
    for _ in range(depth):
        spaces_indent = spaces_indent + '  '

    # Final element, place all remaining spaces at the end.
    if depth > len(groups):
        if evaluate_combination(pattern, combination + ["."] * spaces, spaces_indent):
            return 1
        else:
            return 0

    # This is the first element, start a loop from 0 to maximum
    elif depth == 0:
        matches = 0
        for i in range(0, spaces + 1):
            matches += get_combinations(pattern, combination + ["."] * i, groups, spaces - i, depth + 1)
        
        return matches

    # Group items except the last one
    elif depth > 0 and depth < len(groups):
        matches = 0
        for i in range(1, spaces + 1):
            matches += get_combinations(pattern, combination + ["#"] * groups[depth - 1] + ["."] * i, groups, spaces - i, depth + 1)
        
        return matches
    
    # The final group item
    else:
        # Add no extra spaces
        return get_combinations(pattern, combination + ["#"] * groups[depth - 1], groups, spaces, depth + 1)
        

combinations = 0
for line in inputdata:
    parts = line.strip().split(" ")
    
    pattern = []
    for i in parts[0]:
        pattern.append(i)

    groups = []
    places = 0
    
    for i in parts[1].split(","):
        groups.append(int(i))
        places += int(i)

    spaces = len(pattern) - places

    combinations += get_combinations(pattern, [], groups, spaces, 0)
	
print(f"Part 1: {combinations}")


# Part 2

# Currently a simple implementation of multiplying the length of all the
# inputes by 5. Obviously not a reasonable solution which takes a long
# time to even complete the test data. Needs a smarter solution.

#combinations = 0
#for line in inputdata:
#    parts = line.strip().split(" ")
#    
#    expanded_left = parts[0] + "?" + parts[0] + "?" + parts[0] + "?" + parts[0] + "?" + parts[0]
#
#    pattern = []
#    for i in expanded_left:
#        pattern.append(i)
#    print(pattern)
#
#    groups = []
#    places = 0
#    for x in range(0,5):
#        for i in parts[1].split(","):
#            groups.append(int(i))
#            places += int(i)
#    
#    spaces = len(pattern) - places
#    
#    combinations += get_combinations(pattern, [], groups, spaces, 0)
#	
#print(f"Part 2: {combinations}")

exit()
