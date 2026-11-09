<?php

$filename   = $argv[1];
$handle     = fopen($filename, 'r');
$lines      = explode("\n", fread($handle, filesize($filename)));

fclose($handle);

$valid_passphrases_1 = 0;
$valid_passphrases_2 = 0;

foreach ($lines as $line) {

	$values = preg_split("/\s+/", $line);

	// For Part 2, create array of values with each word sorted alphabetically.

	$values_p2 = [];
	foreach ($values as $value) {
		$chars = str_split($value);
		sort($chars);
		$values_p2[] = implode('', $chars);
	}

	// Check passphrase for Part 1
	$valid = true;
	foreach (array_count_values($values) as $count) {
		if ($count > 1) {
			$valid = false;
			break;
		}
		
	}

	if ($valid) {
		$valid_passphrases_1++;
	}
	
	// Check passphrase for Part 2
	$valid = true;
	foreach (array_count_values($values_p2) as $count) {
		if ($count > 1) {
			$valid = false;
			break;	
		}

	}

	if ($valid) {
		$valid_passphrases_2++;
	}

}

echo "Solution for Part 1: {$valid_passphrases_1}\n";
echo "Solution for Part 2: {$valid_passphrases_2}\n";
