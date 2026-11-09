<?php

$puzzle_input = 1024; // Replace with puzzle input.

// Initialize grid with the first point
$grid = ['0|0' => 1];

$directions = [
	[1,0],	// Right
	[0,1],	// Up
	[-1,0],	// Left
	[0,-1]	// Down
];

// The current direction, 0 - 3 as per the above array.
$dir = 0;

// The starting position.
$pos = [0,0];

$momentum		= 1;
$flag			= 0; // Set to 1 when solved.

// Stores the exact value for the puzzle. The `break 2` command should prevent the script 
// calculating beyond the required result, but this guarantees we get the value we want.
$part2_value	= 0; 

while ($flag == 0) {

	// The key to forming the spiral grid. It grows the same amount on two sides before
	// increasing the side length.
	for ($j = 1; $j <= 2; $j++) {
		
		// Build one side of the grid
		for ($i = 1; $i <= $momentum; $i++) {
			
			$sum = 0;
			
			$pos[0] += $directions[$dir][0];
			$pos[1] += $directions[$dir][1];

			// Add up the values of surrounding 8 grid spaces.
			for ($x = $pos[0] - 1;$x <= $pos[0] + 1;$x++) {
				for ($y = $pos[1] - 1;$y <= $pos[1] + 1;$y++) {

					// By nature of the puzzle, most elements don't exist. Check first then sum.
					if (array_key_exists(strval($x) . '|' . strval($y), $grid)) {
						$sum += $grid[strval($x) . '|' . strval($y)];			
					}
				}	
			}
			
			$grid[$pos[0] . "|" . $pos[1]] = $sum;
			
			if ($sum > $puzzle_input) {
				$flag			= 1;
				$part2_value	= $sum;
				break 2;
			}

		}

		// Cycle the direction for the next side of the spiral grid.
		$dir++;
		if ($dir > 3) {
			$dir = 0;
		}

	}

	// Increase the momentum. This happens only after two iterations as per the loop above.
	$momentum++;
	
}

echo "Solution for Part 2: {$part2_value}\n";
