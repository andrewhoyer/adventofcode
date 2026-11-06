<?php

$puzzle_input	= 1024;

// Initialize grid with the first point
$grid = [1 => [0,0]];

$directions = [
	[1,0],	// Right
	[0,1],	// Up
	[-1,0],	// Left
	[0,-1]	// Down
];

$dir = 0;

// The starting position.
$pos = [0,0];

$counter	= 1; // Array begins with two elements
$momentum	= 1;


while ($counter <= $puzzle_input) {

	// The key to forming the spiral grid. It grows the same amount on two sides before
	// increasing the side length
	for ($j = 1; $j <= 2; $j++) {
		
		// Build one side of the grid
		for ($i = 1; $i <= $momentum; $i++) {
			
			$counter++;
			
			$pos[0] += $directions[$dir][0];
			$pos[1] += $directions[$dir][1];

			$grid[$counter] = [$pos[0], $pos[1]];

		}

		// Cycle the direction for the next side of the spiral grid
		$dir++;
		if ($dir > 3) {
			$dir = 0;
		}

	}

	// Increase the momentum. This happens only after two iterations as per the loop above
	$momentum++;
	
}

// The distance from 0,0 is the the absolute values of x and y of any location.
$distance = abs($grid[$puzzle_input][0]) + abs($grid[$puzzle_input][1]);

echo "Solution for Part 1: {$distance}\n";
