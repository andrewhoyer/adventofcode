import time

inputdata = open("puzzle-input.txt", "r").readlines()

outcomes = {
'X': {'wins':'Z', 'loses':'Y', 'ties':'X', 'score':1}, 
'Y': {'wins':'X', 'loses':'Z', 'ties':'Y', 'score':2}, 
'Z': {'wins':'Y', 'loses':'X', 'ties':'Z', 'score':3}
}

results_against = {
'X': {'wins':'Z', 'loses':'Y', 'ties':'X', 'score':1}, 
'Y': {'wins':'X', 'loses':'Z', 'ties':'Y', 'score':2}, 
'Z': {'wins':'Y', 'loses':'X', 'ties':'Z', 'score':3}
}

results = {'X':'wins', 'Y':'ties', 'Z':'loses'}
 
def follow_strategy(part):

	total_score = 0
	wins        = 0
	losses      = 0
	ties        = 0
	
	for row in inputdata:
		rps_row = row.strip()
		rps_row = rps_row.replace('A','X')
		rps_row = rps_row.replace('B','Y')
		rps_row = rps_row.replace('C','Z')
		rps_parts = rps_row.split(' ')

		if part == 1:
			if outcomes[rps_parts[1]]['wins'] == rps_parts[0]:
				wins = wins + 1
				total_score = total_score + 6 + outcomes[rps_parts[1]]['score']
			elif outcomes[rps_parts[1]]['ties'] == rps_parts[0]:
				ties = ties + 1
				total_score = total_score + 3 + outcomes[rps_parts[1]]['score']
			else:
				losses = losses + 1
				total_score = total_score + 0 + outcomes[rps_parts[1]]['score']
		
		else:
			result = results_against[rps_parts[0]][results[rps_parts[1]]]
				
			if result == 'X':
				losses = losses + 1
				total_score = total_score + 1
			elif result == 'Y':
				ties = ties + 1
				total_score = total_score + 2
			else:
				wins = wins + 1
				total_score = total_score + 3
		
			if rps_parts[1] == 'Z':	
				total_score = total_score + 6
			elif rps_parts[1] == 'Y':	
				total_score = total_score + 3
			elif rps_parts[1] == 'X':	
				total_score = total_score + 0
		
		print("Wins: ", wins, end=' ')
		print("Ties: ", ties, end=' ')
		print("Loss: ", losses, end=' ')
		print("Score: ", total_score, end='\r')
		time.sleep(0.001)	

	print("\r\n")

	print("Total Score: ", total_score, end='\n\n')

print("Day 2 Part 1")
follow_strategy(1)

print("Day 2 Part 2")
follow_strategy(2)

exit()
