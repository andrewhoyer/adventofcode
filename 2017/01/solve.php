<?php

$filename   = $argv[1];
$handle     = fopen($filename, 'r');
$lines      = explode("\n", fread($handle, filesize($filename)));

fclose($handle);

// Create an array of each individual character.
$values = str_split($lines[0]);

// Reduce duplication of code by looping part 1 and 2.
foreach ([1,2] as $part) {

	$sum = 0;

	// Go through the full list and compare with specified values.
	for ($i = 0; $i < count($values); $i++) {

		// Choose the target distance by the part. The actions are the same.
		if ($part == 1) {
			$target = $i + 1;
		} else {
			$target = $i + (count($values) / 2);
		}

		// Treat the array like a circle, going back to the start if greater than the total.
		if ($target > count($values) - 1) {
			$target -= count($values);
		}

    if ($values[$i] == $values[$target]) {
        $sum += $values[$i];    
   	}

	}

	echo "Solution for Part {$part}: {$sum}\n";

}

