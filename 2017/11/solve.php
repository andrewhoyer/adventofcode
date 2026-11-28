<?php

$filename   = $argv[1];
$handle     = fopen($filename, 'r');
$lines      = explode("\n", fread($handle, filesize($filename)));

fclose($handle);

$directions = preg_split("/,/", $lines[0]);

$position = [0,0];

$furthest = 0; // Part 2

foreach ($directions as $direction) {

	$move = get_movement_for_direction($direction, $position);

	$position[0] += $move[0];
	$position[1] += $move[1];

	// Part 2
	$distance = calculate_distance($position);

	if ($distance > $furthest) {
		$furthest = $distance;
	}

}

echo "Solution for Part 1: " . calculate_distance($position) . "\n";
echo "Solution for Part 1: " . $furthest . "\n";


/* For any direction and position, return the correct amount
 to add to the x and y position. This differs from a grid in
 that depending on what the x position is, y may or may not
 change due to the zig zag pattern of the hex grid. */
function get_movement_for_direction($dir, $pos) {

	$movement = [0,0];

	if ($dir == 'n') {
		$movement[0] = 0;
		$movement[1] = -1;		

	} elseif ($dir == 'ne') {
		$movement[0] = 1;
		if ($pos[0] % 2 == 0) {
			$movement[1] = 0;
		} else {
			$movement[1] = -1;
		}

	} elseif ($dir == 'nw') {
		$movement[0] = -1;
		if ($pos[0] % 2 == 0) {
			$movement[1] = 0;
		} else {
			$movement[1] = -1;
		}

	} elseif ($dir == 's') {
		$movement[0] = 0;
		$movement[1] = 1;

	} elseif ($dir == 'se') {
		$movement[0] = 1;
		if ($pos[0] % 2 == 0) {
			$movement[1] = 1;
		} else {
			$movement[1] = 0;
		}
		
	} elseif ($dir == 'sw') {
		$movement[0] = -1;
		if ($pos[0] % 2 == 0) {
			$movement[1] = 1;
		} else {
			$movement[1] = 0;
		}

	}

	return $movement;

}

/* Move one hex grid at a time back to the 0,0 coordinate,
 returning the total number of moves. The primary key to
 this solution is that for any move, there must always be
 a north or south. Whether or not east or west is used
 depends on the position. For example, if the search reaches
 the same vertical row (x), all that needs to be changed is
 the y value until 0,0 is reached. */
function calculate_distance($pos) {

	$counter = 0;
	while ($pos[0] != 0 || $pos[1] != 0) {

		$mover = '';
		if ($pos[1] <= 0) {
			$mover .= 's';

			if ($pos[0] > 0) {
				$mover .= 'w';
			} elseif ($pos[0] < 0) {
				$mover .= 'e';
			}
		} elseif ($pos[1] > 0) {
			$mover .= 'n';

			if ($pos[0] > 0) {
				$mover .= 'w';
			} elseif ($pos[0] < 0) {
				$mover .= 'e';
			}
		}
		
		$move = get_movement_for_direction($mover, $pos);
		
		$pos[0] += $move[0];
		$pos[1] += $move[1];

		$counter++;
	}

	return $counter;
	
}
