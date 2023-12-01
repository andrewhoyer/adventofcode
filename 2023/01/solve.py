import sys

argv1 = sys.argv[1] # Filename of puzzle data passed as parameter

inputdata = open(argv1, "r").readlines()

# Translates a line of text with words to text with a numeric value.
# While not as clean as solutions using regex or other ideas, it does
# solve the problem by injecting the number, and maintaining the letters
# to the left and right which may be part of other words.
def translate_line(line):

    line = line.replace('one','o1e')
    line = line.replace('two','t2o')
    line = line.replace('three','t3e')
    line = line.replace('four','f4r')
    line = line.replace('five','f5e')
    line = line.replace('six','s6x')
    line = line.replace('seven','s7n')
    line = line.replace('eight','e8t')
    line = line.replace('nine','n9e')

    return line

def solve(part):

    sum         = 0
    firstnum    = ''
    lastnum     = ''
    
    for line in inputdata:

        if part == 2:
            line = translate_line(line)
        
        firstflag = False

        for instruction in line.strip():
            if instruction.isdigit():
                if firstflag == False:
                    firstflag   = True
                    firstnum    = instruction
                    lastnum     = instruction
                else:
                    lastnum     = instruction
        
        sum += int(f"{firstnum}{lastnum}")

    print(f"Solution for Part {part}: {sum}")

solve(1)
solve(2)