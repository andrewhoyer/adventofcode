<?php

$filename   = $argv[1];
$handle     = fopen($filename, 'r');
$lines      = explode("\n", fread($handle, filesize($filename)));

fclose($handle);

$instructions = [];
foreach ($lines as $line) {
	$instructions[] = intval($line);
}

reset ($instructions);

$count = 0;

// Continue while the array pointer is within bounds, or if the value is 0.
// There's probably a better way to consider 0. Find out later.
while (! current($instructions) === false || current($instructions) === 0) {

	// The lines using $adjust are the changes to solve Part 2.
	$adjust = 1;

	$move = current($instructions);
	
	if ($move >= 3) {
		$adjust = -1;
	}

	$instructions[key($instructions)] = $move + $adjust;

	while ($move != 0) {

		if ($move > 0) {
			next($instructions);
			$move--;
		} else {
			prev($instructions);
			$move++;
		}

	}

	$count++;
}

echo "Solution for Part 2: {$count}\n";
