import sys

argv1 = sys.argv[1] # Filename of puzzle data passed as parameter

inputdata = open(argv1, "r").readlines()

# Set up arrays with times and distances of races
times = []
for i in inputdata[0].split(":")[1].strip().split(" "):
    if i != "":
        times.append(int(i))

distances = []
for i in inputdata[1].split(":")[1].strip().split(" "):
    if i != "":
        distances.append(int(i))

# Calculate all possible win cases based on how long the
# button is held down, avoiding ones where the button
# isn't held at all, and where it's held the entire time.
win_cases = []
for x in range(0, len(times)):
    wins = 0
    for time in range(1, times[x]):

        total_distance = (times[x] - time) * (time)
        
        if total_distance > distances[x]:
            wins += 1

    win_cases.append(wins)

# Do the math.
total = 0
for w in win_cases:
    if total == 0:
        total = w
    else:
        total *= w

print(f"Total number of win cases: {total}")
