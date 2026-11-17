<?php

$filename   = $argv[1];
$handle     = fopen($filename, 'r');

// Process the entire file into an array of individual characters
$input      = str_split(fread($handle, filesize($filename)));

fclose($handle);

$index		= 0;
$score		= 0; // Part 1
$garbage	= 0; // Part 2
$level		= 0;

$mode			= 'none'; // group, garbage
$mode_previous	= 'none';

while ($index < count($input)) {

	if ($input[$index] == '!') {
		// Ignore the ! and any character that comes after it.
		$index += 2;
		continue;
	}

	// There are three possible states. 'none' is outside a group or garbage (or at the start).
	// 'group' is within a group. 'garbage' is within a section of garbage.
	if ($mode == 'none' || $mode == 'group') {
		
		if ($input[$index] == '{') {
			$mode = 'group';
			$level++;
			$index++;
			continue;
		} elseif ($input[$index] == '}') {
			if ($level > 0) {
				$mode = 'group';
				$score += $level;
				$level--;
				$index++;
				continue;
			} elseif ($level == 0) {
				$mode = 'none';
				$mode_previous = 'none';
			}
		} elseif ($input[$index] == '<') {
			$mode_previous = $mode;
			$mode = 'garbage';
			$index++;
			continue;
		} else{
			// When in any state other than garbage, characters other than '{' or '<' are unimportant and can be skipped.
			$index++;
			continue;
		}

	} elseif ($mode == 'garbage') {

		// Garbage text is simple. Anything besides a '>' is counted as garbage and ignored.
		// The exception to this is !> which is handled first thing in the loop.
		if ($input[$index] == '>') {
			// When leaving a garbage tag, it's important to go back to the previous mode,
			// especially as it might not be 'group'.
			$mode = $mode_previous;
		} else {
			$garbage++; // Part 2
			$index++;
			continue;
		}
		
	}

}

echo "Solution for Part 1: " . $score . "\n";
echo "Solution for Part 2: " . $garbage . "\n";
