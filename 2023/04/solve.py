import sys

argv1 = sys.argv[1] # Filename of puzzle data passed as parameter

inputdata = open(argv1, "r").readlines()

def solve():

    points = 0

    for line in inputdata:
        line = line.strip()
        useful_data = line.split(": ")

        card_numbers = useful_data[1].split(" | ")

        winning_numbers = []
        for number in card_numbers[0].strip().split(" "):
            if number != "":
                winning_numbers.append(number)

        your_numbers = []
        for number in card_numbers[1].strip().split(" "):
            if number != "":
                your_numbers.append(number) 

        card_score = 0
        for number in your_numbers:
            
            if number in winning_numbers:
                
                if card_score == 0:
                    card_score = 1
                else:
                    card_score = card_score * 2

        points += card_score

    print(f"Points for Part 1: {points}")

solve()