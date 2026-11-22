<?php

$filename   = $argv[1];
$handle     = fopen($filename, 'r');
$lines      = explode("\n", fread($handle, filesize($filename)));

fclose($handle);

$values = preg_split("/,/", $lines[0]);

$sequences = [];
foreach ($values as $value) {
	$sequences[] = intval($value);
}

// Create the starting range of circular values.
$circular = range(0,255); // Input
//$circular = range(0,4); // Test

// Used to check for or move to the start or end of an array when the limit is reached.
$high_index		= count($circular) - 1;
$circular_count	= count($circular);

$position	= 0;
$skip		= 0;

// Loop through the sequences in the input data.
foreach ($sequences as $sequence) {

	// Calculate the array index that the left side of the switch
	// should end when reached.
	$target = $position + floor($sequence / 2);
	
	if ($target > $high_index) {
		$target -= $circular_count;
	}
	
	// Calculate the array index of the last value that will be switched.
	// Together these values will be incremented and decremented after
	// being switched, until the target is reached.
	$second_index = $sequence + $position - 1;

	if ($second_index > $high_index) {
		$second_index -= $circular_count;
	}

	// DO the switch. Proceed until $i is equal to the %target.	
	for ($i = $position;$target != $i;$i++ ) {

		if ($i > $high_index) {
			$i = 0;
		}

		// FIXME: As it turns out, the while condition in the main for loop
		// never actually fails because $i++ brings it back to 1 after being
		// reset to 0 by the above check. This only happens in cases where
		// the target is 0. There's probably a better way to handle the loop,
		// perhaps simply with a while loop.
		if ($i == $target) {
			break;
		}

		// Get the values of the array elements as we'll swap them with each other.
		$first	= $circular[$i];
		$second	= $circular[$second_index];

		// Swap them.
		$circular[$i]				= $second;
		$circular[$second_index]	= $first;
		

		// Bring the right index down, and move to the end if needed.
		$second_index--;

		if ($second_index < 0) {
			$second_index = $high_index;
		}
		
	}
	
	// As per the instructions, move the position forward the number in the current
	// sequence, plus the skip value. Move to the corresponding index near the
	// beginning if needed.
	$position = $position + $sequence + $skip;
	if ($position > $high_index) {
		$position -= $circular_count;
	}
	
	// Skip incremements each sequence.
	$skip++;

}

echo "Solution for Part 1: " . $circular[0] * $circular[1] . "\n";
