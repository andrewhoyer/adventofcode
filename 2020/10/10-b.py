inputdata = open("input-data.txt", "r").readlines()

# Get the adapters into an array of integers
adapters = []

for line in inputdata:
	adapters.append(int(line.strip()))

adapters = sorted(adapters)

index        = 0
maxadapter   = adapters[len(adapters)-1]
combinations = 0
depth        = 0
tree         = {}

def checkadapters(thisadapter, combinations, depth):
	
	# Indenting really helps with debugging, to show search depth level
	#spaces = ''
	#for _ in range(depth):
	#	spaces = spaces + ' '
	
	#print("{}{}".format(spaces,thisadapter))
	
	#print("\nCalled checkadapters({},{})".format(thisadapter, combinations))
	nextinchain = []
	
	# Return with an increment as soon as the max value is reached
	if thisadapter == maxadapter:
		return combinations + 1
	else:

		nextinchain = []
		for adapter in adapters:
			if adapter - thisadapter <= 3 and adapter > thisadapter:
				nextinchain.append(adapter)
								
		#print("Adapters to be followed: {}".format(nextinchain))
	
		depth = depth + 1
		
		for chain in nextinchain:
			
			# The key to the solution! 
			# Once a tree has been calculated, never do it again, just reuse the value
			if chain in tree.keys():
				combinations = combinations + tree[chain]
			else:
				combinations = checkadapters(chain, combinations, depth)
				tree[chain] = combinations
		
		return combinations
	
# Fire up the recursive function!
combinations = checkadapters(0, combinations, depth)

print(combinations)
