from itertools import count
import sys
import pprint
pp = pprint.PrettyPrinter(indent=2)

argv1 = sys.argv[1] # Filename of puzzle data passed as parameter

inputdata = open(argv1, "r").readlines()

values = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 11,
    'T': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2
}

def compare_hands(hand1, hand2):

    for i in range(0, 5):
        if values[hand1[i]] > values[hand2[i]]:
            return 1
        elif values[hand1[i]] < values[hand2[i]]:
            return 2
        elif values[hand1[i]] == values[hand2[i]]:
            continue


def hand_type(cards):

    uniques = {}

    for card in cards:
        if card in uniques:
            uniques[card] += 1
        else:
            uniques[card] = 1

    hand_type = 0

    if len(uniques) == 1:
        hand_type = 1

    if len(uniques) == 2:
        for unique in uniques:
            if uniques[unique] == 4:
                hand_type = 2
            
            if uniques[unique] == 3:
                hand_type = 3

    if len(uniques) == 2:
        for unique in uniques:
            if uniques[unique] == 4:
                hand_type = 2
            
            if uniques[unique] == 3:
                hand_type = 3

    if len(uniques) == 3:
        for unique in uniques:
            if uniques[unique] == 3:
                hand_type = 4
            
            if uniques[unique] == 2:
                hand_type = 5

    if len(uniques) == 4:
            hand_type = 6

    if len(uniques) == 5:
            hand_type = 7            
    
    return hand_type


hands = []

for hand in inputdata:

    hand_details = {}
    cards, bid = hand.strip().split(" ")

    hand_details['cards'] = cards
    hand_details['bid'] = int(bid)
    
    card_list = []
    for card in cards:
        card_list.append(card)

    hand_details['card_list'] = card_list
    
    hand_details['type'] = hand_type(card_list)

    hands.append(hand_details)

needs_ordering = True

while (needs_ordering == True):
    
    needs_ordering = False

    counter = 0
    for hand in range(0,len(hands) - 1):
    
        if hands[counter]['type'] < hands[counter + 1]['type']:
            hands[counter], hands[counter + 1] = hands[counter + 1],  hands[counter] 
            needs_ordering = True
        elif hands[counter]['type'] == hands[counter + 1]['type']:
            if compare_hands(hands[counter]['card_list'], hands[counter + 1]['card_list']) == 1:
                hands[counter], hands[counter + 1] = hands[counter + 1],  hands[counter] 
                needs_ordering = True

        counter += 1

total = 0

counter = 1
for hand in hands:
    
    total += (hand['bid'] * counter)
    print(f"{counter} : {total}")
    counter += 1
    
print(f"Total score: {total}")

exit()
