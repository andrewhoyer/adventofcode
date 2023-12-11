import sys
import pprint
pp = pprint.PrettyPrinter(indent=2)

argv1 = sys.argv[1] # Filename of puzzle data passed as parameter

inputdata = open(argv1, "r").readlines()

def are_all_zeros(sequence):

    for num in sequence:
        if num != 0:
            return False
    
    return True

sum_part1 = 0
sum_part2 = 0

for line in inputdata:
    sequences = []
    sequence = []
    for num in line.strip().split(" "):
        sequence.append(int(num))
    
    sequences.append(sequence)

    counter = 0
    flag = False

    # Add sequences to the array until one row is all zeros
    while flag == False:
        next_sequence = []
        for num in range(0, len(sequences[counter]) - 1):

            next_sequence.append(sequences[counter][num + 1] - sequences[counter][num])

        sequences.append(next_sequence)
        

        flag = are_all_zeros(next_sequence)
        counter += 1
    
    # From the bottom up, inserting values on the left and right sides of each row. 
    for num in range(len(sequences) -1 , 0, -1):
        
        # Part 1
        sequences[num - 1].append(sequences[num][-1] + sequences[num - 1][-1])

        # Part 2
        sequences[num - 1].insert(0, sequences[num - 1][0] - sequences[num][0])

    sum_part1 += sequences[0][-1]
    sum_part2 += sequences[0][0]


print(f"Part 1 Solution: {sum_part1}")
print(f"Part 2 Solution: {sum_part2}")

exit()
