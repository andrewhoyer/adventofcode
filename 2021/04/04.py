import re

# FUNCTIONS

# Checks a card for completion of any row or column
def checkcard(card):
	
	# Check rows
	for cardrow in card:
		rowcomplete = True
		for index, value in enumerate(cardrow):
			if cardrow[index] != -1:
				rowcomplete = False
				break
				
		if rowcomplete == True:
			return True
	
	# Check columns
	for i in range(0,5):
		colcomplete = True
		for cardrow in card:
			if cardrow[i] != -1:
				colcomplete = False
				break
				
		if colcomplete == True:
			return True
	
	# Default return is False		
	return False
	

# Calculates the puzzle score for a card
def calculate(card, drawnumber):
	
	cardsum = 0
	for cardrow in card:
		for index, value in enumerate(cardrow):
			if cardrow[index] != -1:
				cardsum += cardrow[index]

	print("Sum of unmarked numbers ({}) multiplied by the last drawn number ({}): {}".format(cardsum, drawnumber, cardsum * drawnumber))
	


if __name__ == "__main__":
	
	inputdata = open("input-data.txt", "r").read()

	# Split data into sections, pull out the number list, then remove it
	sections = inputdata.split("\n\n")
	bingonumbers = sections[0].strip().split(",")
	sections.pop(0)

	# Build an array to contain all bingo card data
	cards = []

	for card in sections:
		rowcount = 0
		cardrows = []
		for row in card.split("\n"):
			cardcolumns = []
		
			for item in re.split("\s+", row.strip()):
				cardcolumns.append(int(item))
		
			rowcount += 1
		
			cardrows.append(cardcolumns)

		cards.append(cardrows)

	cardscompleted = 0
	completedcards = []

	for draw in bingonumbers:
	
		if cardscompleted == len(cards):
			break	
	
		drawnumber = int(draw)

		cardcounter = 0

		for card in cards:

			for cardrow in card:

				for index, value in enumerate(cardrow):

					if cardrow[index] == drawnumber:
						cardrow[index] = -1
					
						if checkcard(card) == True:
						
							if cardcounter not in completedcards:
							
								cardscompleted += 1
							
								completedcards.append(cardcounter)
							
								if cardscompleted == 1:
									print("\n****************************\nFirst card completed")
									calculate(card, drawnumber)
									print("****************************\n")
	
								if cardscompleted == len(cards):	
									print("\n****************************\nLast card completed")
									calculate(card, drawnumber)
									print("****************************\n")
						
			cardcounter += 1

	exit()
