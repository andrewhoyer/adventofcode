<?php

$filename   = $argv[1];
$handle     = fopen($filename, 'r');
$sections      = explode("\n\n", fread($handle, filesize($filename)));

fclose($handle);

$ranges = [];

foreach (explode("\n", $sections[0]) as $line) {

    $range = explode('-', $line);
    $ranges[] = [intval($range[0]), intval($range[1])];

}

$count = 0;
foreach (explode("\n", $sections[1]) as $line) {

    $ingredient = intval($line);

    foreach ($ranges as $range) {
        if ($ingredient >= $range[0] && $ingredient <= $range[1]) {
            $count++;
            break;
        }
    }

}

print("Part 1 solution: " . $count . "\n");

$combined = [];
$updates = -1;
while (count($ranges) != 0) {

    $updates = 0;
    $working = array_shift($ranges);

    $removes = [];
    $index = 0;
    foreach ($ranges as $range) {
        
        
        if (($working[0] >= $range[0] && $working[0] <= $range[1]) ||
            ($working[1] >= $range[0] && $working[1] <= $range[1])) {
            
            // Check for any overlap. Extend the range of one to include the other.

            // Store the index of the range to be removed
            $removes[] = $index;

            if ($range[0] < $working[0]) {
                $working[0] = $range[0];
            }

            if ($range[1] > $working[1]) {
                $working[1] = $range[1];
            }

            $count++;
            $updates++;
            
        } else if ( ($working[0] <= $range[0] && $working[1] >= $range[1]) ) {
            // The working range completely includes the checked range.
            $removes[] = $index;
        }

        $index++;

    }

    $combined[] = $working;

    // Working backwards, remove all elements that were merged into others.
    for ($i = count($removes) - 1;$i >= 0;$i--) {
        unset($ranges[$removes[$i]]);
    }

    sort($ranges);

}

$sum = 0;
foreach ($combined as $range) {
    $sum += $range[1] - $range[0] + 1;
}

print("Part 2 solution: " . $sum . "\n");

exit();
