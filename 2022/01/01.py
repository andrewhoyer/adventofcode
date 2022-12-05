inputdata = open("puzzle-input.txt", "r").readlines()

most_calories = 0
calorie_count = 0

elves = []

for row in inputdata:
	
	if row.strip() == '':
		if calorie_count > most_calories:
			most_calories = calorie_count

		elves.append(calorie_count)
		calorie_count = 0
	
	else:
		calorie_count = calorie_count + int(row.strip())

elves.sort()

for calories in elves:
	print("*" * int(calories / 900), calories)

elves.reverse()

print("Part 1 - Most calories carried by an elf: {}".format(most_calories))

print("Part 2 - Calories of top three elves: {}".format(elves[0] + elves[1] + elves[2]))
