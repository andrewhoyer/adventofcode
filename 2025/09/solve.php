<?php

$filename   = $argv[1];
$handle     = fopen($filename, 'r');
$lines      = explode("\n", fread($handle, filesize($filename)));

fclose($handle);

// Generate the list of points on the grid.
$tiles = [];

foreach ($lines as $line) {

    $parts = explode(',', $line);

    $tiles[] = [intval($parts[0]), intval($parts[1])];

}

// Loop through every point, compare it with all others and find the greatest area.

$greatest = 0;

while (count($tiles) != 0) {

    $tile = array_shift($tiles);

    foreach ($tiles as $compare) {

        $area = (abs($tile[0] - $compare[0]) + 1) * (abs($tile[1] - $compare[1]) + 1);

        if ($area > $greatest) {
            $greatest = $area;
        }
    }


}

print("Part 1 solution: " . $greatest . "\n");

exit();
