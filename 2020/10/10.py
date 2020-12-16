inputdata = open("input-data.txt", "r").readlines()

adapters = []

for line in inputdata:
	adapters.append(int(line.strip()))

adapters = sorted(adapters)

print(adapters)

onecounter = 0
threecounter = 0
currentjoltage = 0


for adapter in adapters:
	if adapter - currentjoltage > 3:
		print("too far apart. adapter {}, joltage {}".format(adapter, currentjoltage))
	elif adapter - currentjoltage == 3:
		print("diff 3. adapter {}, joltage {}".format(adapter, currentjoltage))
		threecounter = threecounter + 1
	elif adapter - currentjoltage == 1:
		print("diff 1. adapter {}, joltage {}".format(adapter, currentjoltage))
		onecounter = onecounter + 1
		
	currentjoltage = adapter

# add one for the device's difference
threecounter = threecounter + 1

print("\nones {}, threes {}. Multiplied = {}".format(onecounter, threecounter, onecounter * threecounter))
