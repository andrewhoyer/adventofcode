class LowestCommonMultiple:

	def __init__(self):
		self.lastdepth = {} # Records the value searched the first time at any one depth

		# Records the difference between when each depth is matched. This is the key
		# as matches are achieved at exact intervals.
		self.intervals = {}
	
	def compare_next_value(self, values, check_value, depth, increaseby):
	
		# Indenting really helps with debugging, to show search depth level
		spaces = ''
		for _ in range(depth):
			spaces = spaces + '  '
			
		# Does the check value divide evently into the value at the current depth?
		if check_value % values[depth] == 0:
			
			# Check the next iteration, unless it's the last item in the array
			if depth < len(values) - 1:
				
				if depth in self.lastdepth:
					if depth not in self.intervals:
						# Record the difference between the value to be checked and the value
						# first checked at this depth
						self.intervals[depth] = check_value - self.lastdepth[depth]
					
					# Search the next value in the array, using the interval as
					# the amount to increase by. 
					return self.compare_next_value(values, check_value, depth + 1, self.intervals[depth])
					
				else:
					# The first time any depth is reached, log the value checked
					self.lastdepth[depth] = check_value
					
					return self.compare_next_value(values, check_value, depth + 1, increaseby)
				
			else:
				# Reached the end of the array, and the lowest common multiple has been found
				return 0
				
		else:
			# If it's not a match, send back the next number to check. This greatly reduces the 
			# time needed to find common multiples
			return check_value + increaseby

	def find_common(self, values):

		# Reset
		self.lastdepth = {}
		self.intervals = {}

		# Set the first value to be checked against
		check_value = values[0]

		depth = 0

		while True:

			increaseToValue = self.compare_next_value(values, check_value, depth, values[depth])
			
			if increaseToValue == 0:
				# Lowest common multiple is found
				return check_value
			
			else:
				# Update the value to be checked, then repeat the process
				check_value = increaseToValue

