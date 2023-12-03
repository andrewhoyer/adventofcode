import sys

argv1 = sys.argv[1] # Filename of puzzle data passed as parameter

inputdata = open(argv1, "r").readlines()

def solve():

    sum_ids     = 0 # Part 1
    sum_powers  = 0 # Part 2

    # Cube limits for Part 1
    limits = {
        'red': 12,
        'green': 13,
        'blue': 14
    }
    
    for line in inputdata:
        
        # Part 1
        possible_game = True

        # Minimum cubes required for Part 2
        cube_minimums = {
            'red': 0,
            'green': 0,
            'blue': 0
        }

        line = line.strip()

        game_meta, colors = line.split(': ')

        game_id = int(game_meta.split(' ')[1])
        
        draws = colors.split('; ')

        for draw in draws:
            draw_colors = draw.split(', ')

            for color_count in draw_colors:
                cube_count, cube_color = color_count.split(' ')

                # Part 1 check
                if int(cube_count) > limits[cube_color]:
                    possible_game = False
                
                # Part 2 check
                if int(cube_count) > cube_minimums[cube_color]:
                    cube_minimums[cube_color] = int(cube_count)
        
        # Part 1 calculation
        if possible_game == True:
            sum_ids += game_id

        # Part 2 calculation
        sum_powers += cube_minimums['blue'] * cube_minimums['green'] * cube_minimums['red']

    return sum_ids, sum_powers

part1, part2 = solve()
print(f"Solution for Part 1: {part1}")
print(f"Solution for Part 2: {part2}")
