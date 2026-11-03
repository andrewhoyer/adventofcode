<?php

$filename   = $argv[1];
$handle     = fopen($filename, 'r');
$lines      = explode("\n", fread($handle, filesize($filename)));

fclose($handle);

$checksum = 0;
$checksum_p2 = 0;

foreach ($lines as $line) {
	
	// Test data uses /\s+/ while input data uses /\t+/ 
	$values = preg_split("/\t+/", $line);
	
	// Convert text values into integers
	$values_int = [];

	foreach ($values as $value) {
		$values_int[] = intval($value);
	}

	// Important to use sort() over other functions as it reorders the array keys
	sort($values_int);

	// Calculate part 1 checksum
	// Simple high minus low
	$checksum += array_last($values_int) - array_first($values_int);

	// Calculate part 2 checksum
	// Start with the largest number, working down, checking for even division with all lower numbers
	for ($big = count($values_int) - 1; $big > 0; $big--) {
		for ($small = $big - 1; $small >= 0; $small--) {
			
			if ($values_int[$big] % $values_int[$small] == 0) {
				$thisval	  = ($values_int[$big] / $values_int[$small]);
				$checksum_p2 += $thisval;
				break 2;
			}

		}
	}

}

echo "Solution for Part 1: {$checksum}\n";
echo "Solution for Part 2: {$checksum_p2}\n";
