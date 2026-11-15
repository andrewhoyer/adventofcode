<?php

$filename   = $argv[1];
$handle     = fopen($filename, 'r');
$lines      = explode("\n", fread($handle, filesize($filename)));

fclose($handle);

$programs = [];

// Build the entire input data into an array.
foreach ($lines as $line) {
	if (str_contains($line, "->")) {
		
		// The program name and weight
		$program_details = explode(' ', explode(" -> ", $line)[0]);
		
		$weight = $program_details[1];
		$weight = preg_replace("/[\(\)]/", "", $weight);

		// The list of all programs that are stacked on the above program.
		$stacked = explode(', ', explode(" -> ", $line)[1]);

		$programs_stacked = [];

		// Add all stacked programs to another list.
		foreach ($stacked as $program) {
			$programs_stacked[] = $program;
		}

		$programs[$program_details[0]] = [
			'weight'	=> intval($weight),
			'subs'		=> $programs_stacked
		];
		
	} else {

		// These are all programs at the very top level.
		// The program name and weight.
		$program_details = explode(" ", $line);

		$weight = $program_details[1];
		$weight = preg_replace("/[\(\)]/", "", $weight);

		$programs[$program_details[0]] = [
			'weight' => intval($weight)
		];

	}
}

// Use the result of Part 1, or use the lowest value from the sample data.
list_weights('enter_p1_answer', 0, '');

// The recursive function that explores the tree and outputs warnings when 
// it detects an inconsistent value. Note that it will output warnings all
// the way down the tree so you can follow the path. Note: This program
// does not provide you with the actual puzzle solution. It just points you
// to the right place and you need to calculate it yourself.
function list_weights($name, $level, $caller) {

	global $programs;

	if (array_key_exists('subs', $programs[$name])) {

		$total_weight = $programs[$name]['weight'];

		$compare_weight = 0;
		foreach ($programs[$name]['subs'] as $sub) {

			$check_weight = list_weights($sub, $level + 1, $name);

			if ($compare_weight == 0) {
				$compare_weight = $check_weight;
			} else {
				if ($compare_weight != $check_weight) {
					echo(str_repeat("   ", $level + 1) . "IMBALANCE DETECTED name: " . $name . " weight: " . $check_weight . " caller: " . $caller . "\n");
				}
			}

			$total_weight += $check_weight;
		}

		echo(str_repeat("   ", $level) . $name . " " . $total_weight . "\n");

		return $total_weight;

		
	} else {

		$total_weight = $programs[$name]['weight'];
		echo(str_repeat("   ", $level) . $name . " " . $total_weight . "\n");

		return $total_weight;
	}

}







/*
foreach ($programs as $program) {

	// As soon as we find the program that isn't in the stacked list, we have our answer!
	if (! in_array($program, $programs_stacked)) {
		echo "Solution for Part 1: " . $program . "\n";
		break;
	}

}
*/
