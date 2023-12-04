import sys

argv1 = sys.argv[1] # Filename of puzzle data passed as parameter

inputdata = open(argv1, "r").readlines()

def solve():

    # Instead of changing the solution greatly from Part 1, this solution
    # uses an additional array (card_number_totals) that simply tracks
    # how many of each card are in the pile. 
    winning_cards       = []
    your_cards          = []
    card_number_totals  = []

    # Build all of the arrays using the input data.
    for line in inputdata:
        line = line.strip()
        useful_data = line.split(": ")

        card_numbers = useful_data[1].split(" | ")

        winning_numbers = []
        for number in card_numbers[0].strip().split(" "):
            if number != "":
                winning_numbers.append(number) 
        
        winning_cards.append(winning_numbers)

        your_numbers = []
        for number in card_numbers[1].strip().split(" "):
            if number != "":
                your_numbers.append(number) 

        your_cards.append(your_numbers)

        card_number_totals.append(1)

    # Iterate through the the range corresponding to the totals
    # array (but not the array itself as it is modified), and 
    # increase the totals for later cards.
    for card in range(0, len(card_number_totals)):
        
        counter = card_number_totals[card]

        while (counter > 0):
            card_score = 0

            # Reference the arrays containing the card data to
            # determine matches.
            for number in your_cards[card]:
                if number in winning_cards[card]:
                    card_score += 1
            
            # Increase the elements in the totals array following
            # the current one being processed.
            if card_score > 0:
                for i in range(card + 1, card + card_score + 1):
                    card_number_totals[i] += 1
           
            counter -= 1

    # Finally, sum all elements of the totals array.
    total_cards = 0
    for cards in card_number_totals:
        total_cards += cards

    print(f"Total number of cards for Part 2: {total_cards}")

solve()