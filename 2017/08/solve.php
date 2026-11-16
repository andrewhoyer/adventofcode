<?php

$filename   = $argv[1];
$handle     = fopen($filename, 'r');
$lines      = explode("\n", fread($handle, filesize($filename)));

fclose($handle);

$registers = [];
$instructions = [];

foreach ($lines as $line) {
	$parts = explode(' ', $line);
	
	$instructions[] = $parts;

	if (! array_key_exists($parts[0], $registers)) {
		$registers[$parts[0]] = 0;
	}

	if (! array_key_exists($parts[4], $registers)) {
		$registers[$parts[0]] = 0;
	}
}


// For Part 2
$highest_register_ever = 0;

foreach ($instructions as $instruction) {
	
	$proceed = false;

	// Verify the conditional.

	if ($instruction[5] == '<') {
		if (intval($registers[$instruction[4]]) < intval($instruction[6])) {
			$proceed = true;
		} 
	} elseif ($instruction[5] == '>') {
		if (intval($registers[$instruction[4]]) > intval($instruction[6])) {
			$proceed = true;
		} 
	} elseif ($instruction[5] == '<=') {
		if (intval($registers[$instruction[4]]) <= intval($instruction[6])) {
			$proceed = true;
		} 
	} elseif ($instruction[5] == '>=') {
		if (intval($registers[$instruction[4]]) >= intval($instruction[6])) {
			$proceed = true;
		} 
	} elseif ($instruction[5] == '==') {
		if (intval($registers[$instruction[4]]) == intval($instruction[6])) {
			$proceed = true;
		} 
	} elseif ($instruction[5] == '!=') {
		if (intval($registers[$instruction[4]]) != intval($instruction[6])) {
			$proceed = true;
		} 
	}

	// If the condition is valid, process the instruction.

	if ($proceed) {
		if ($instruction[1] == 'dec') {
			$registers[$instruction[0]] = $registers[$instruction[0]] - intval($instruction[2]);
		} elseif ($instruction[1] == 'inc') {
			$registers[$instruction[0]] = $registers[$instruction[0]] + intval($instruction[2]);

			// Part 2
			if ($registers[$instruction[0]] > $highest_register_ever) {
				$highest_register_ever = $registers[$instruction[0]];
			}
		}	
	}
}


// Part 1. Find the highest register value.
$highest = array_first($registers);

foreach ($registers as $register) {
	if ($register > $highest) {
		$highest = $register;
	}
}

echo "Solution for Part 1: " . $highest . "\n";
echo "Solution for Part 2: " . $highest_register_ever . "\n";
