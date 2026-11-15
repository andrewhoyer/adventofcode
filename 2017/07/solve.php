<?php

$filename   = $argv[1];
$handle     = fopen($filename, 'r');
$lines      = explode("\n", fread($handle, filesize($filename)));

fclose($handle);

$programs			= [];
$programs_stacked	= [];

// The idea behind this solution is simple. Look for a program that 
// is not listed as being above another program. That's the lowest
// program in the stack. This becomes the starting point for Part 2.

foreach ($lines as $line) {
	if (str_contains($line, "->")) {
		
		// The list of all programs.
		$programs[] = explode(' ', explode(" -> ", $line)[0])[0];

		// The list of all programs that are stacked on the above program.
		$stacked	= explode(', ', explode(" -> ", $line)[1]);

		// Add all stacked programs to another list.
		foreach ($stacked as $program) {
			$programs_stacked[] = $program;
		}
		
	}
}

foreach ($programs as $program) {

	// As soon as we find the program that isn't in the stacked list, we have our answer!
	if (! in_array($program, $programs_stacked)) {
		echo "Solution for Part 1: " . $program . "\n";
		break;
	}

}
