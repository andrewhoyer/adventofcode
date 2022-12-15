inputdata = open("puzzle-input.txt", "r").readlines()

# Part 1

fully_contained_sections = 0

for row in inputdata:
	sections = row.strip().split(',')
	
	# Check for a complete overlap of either range
	if (int(sections[0].split('-')[0]) >= int(sections[1].split('-')[0]) and \
      int(sections[0].split('-')[1]) <= int(sections[1].split('-')[1])) or \
     (int(sections[1].split('-')[0]) >= int(sections[0].split('-')[0]) and \
      int(sections[1].split('-')[1]) <= int(sections[0].split('-')[1])):
		
		fully_contained_sections = fully_contained_sections + 1

print ("Part 1: Fully contained sections: {}".format(fully_contained_sections))


# Part 1

overlapping_assignments= 0

for row in inputdata:
	sections = row.strip().split(',')

	# Create ranges of both sections for easy comparsion of values
	range1 = range(int(sections[0].split('-')[0]), int(sections[0].split('-')[1]) + 1)
	range2 = range(int(sections[1].split('-')[0]), int(sections[1].split('-')[1]) + 1)
	
	#Loop through one range, stop at the first match
	for i in range1:
		if i in range2:
			overlapping_assignments = overlapping_assignments + 1
			break;

print ("Part 2: Overlapping assignments: {}".format(overlapping_assignments))

exit()
