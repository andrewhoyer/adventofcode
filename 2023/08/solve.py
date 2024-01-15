import sys
import pprint
pp = pprint.PrettyPrinter(indent=2)

argv1 = sys.argv[1] # Filename of puzzle data passed as parameter

inputdata = open(argv1, "r").readlines()

# Get the first line which contains instructions
instructions = inputdata.pop(0).strip()

# Remove the next line which is blank
inputdata.pop(0)

move_list = {}
for line in inputdata:
        parts = line.strip().split(" = ")
        move_list[parts[0]] = parts[1].replace("(", "").replace(")", "").replace(",", "").split(" ")


# Travel through the move list based on the instructions until
# ZZZ is reached, counting the number of steps.

destination = "AAA"

counter = 0
while (destination != "ZZZ"):

    for ch in instructions:
        counter += 1

        if ch == "R":
            destination = move_list[destination][1]
        else:
            destination = move_list[destination][0]
        
        if destination == "ZZZ":
            break

print(f"The number of steps to reach ZZZ is: {counter}")
