import sys

argv1 = sys.argv[1] # Filename of puzzle data passed as parameter

inputdata = open(argv1, "r").readlines()

total_area      = 0
total_ribbon    = 0

for box in inputdata:
    dimensions = []
    for dimension in box.strip().split('x'):
        dimensions.append(int(dimension))
    
    dimensions.sort()

    areas = []
    areas.append(dimensions[0] * dimensions[1])
    areas.append(dimensions[1] * dimensions[2])
    areas.append(dimensions[0] * dimensions[2])

    areas.sort()

    total_area      += areas[0] + 2 * areas[0] + 2 *areas[1] + 2 * areas[2]
    total_ribbon    += 2 * dimensions[0] + 2 * dimensions[1] + dimensions[0] * dimensions[1] * dimensions[2]


print(f"Total area of wrapping paper needed: {total_area}")
print(f"Total length of ribbon needed: {total_ribbon}")
