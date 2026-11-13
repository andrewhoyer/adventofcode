<?php

$filename   = $argv[1];
$handle     = fopen($filename, 'r');
$lines      = explode("\n", fread($handle, filesize($filename)));

fclose($handle);

$values = preg_split("/\t+/", $lines[0]);

$banks = [];
foreach ($values as $value) {
	$banks[] = intval($value);
}

// A way to log each states, and adding the original state.
$states		= [];
$states[]	= implode("-", $banks);

$complete = false;

while (! $complete) {

	$bank = get_highest_bank($banks);
	$move = $banks[$bank];

	$banks[$bank] = 0;

	// Iterate as many times as needed, moving forward in the array and incrementing.
	while ($move > 0) {

		$bank++;

		if ($bank > count($banks) - 1) {
			$bank = 0;
		}

		$banks[$bank] = $banks[$bank] + 1;

		$move--;
	}

	// If the state already existed, exit and report result. Otherwise add state and loop again.
	if (in_array(implode("-", $banks), $states)) {
		$complete = true;	
	} else {
		$states[] = implode("-", $banks);
	}

}

echo "Solution for Part 1: " . count($states) . "\n";

exit;


// Finds the highest bank, preferring earlier array elements
function get_highest_bank($banks) {

	$index = -1;
	$high = -1;

	$counter = 0;
	foreach ($banks as $bank) {
		if ($bank > $high) {
			$high = $bank;
			$index = $counter;
		}
		$counter++;
	}

	return $index;

}
