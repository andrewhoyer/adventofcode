inputdata = open("input-data.txt", "r")
numbers = inputdata.readlines()

complete = False
firstnumber = 0
secondnumber = 0

# Loop through the array, removng one value and comparing it to each of the others

while complete == False:

  firstnumber = int(numbers.pop().strip())

  for number in numbers:
    if firstnumber + int(number.strip()) == 2020:
      secondnumber = int(number.strip())
      complete = True

  if len(numbers) <= 1:
    complete = True

print("{} * {} = {}".format(firstnumber, secondnumber, firstnumber * secondnumber))

