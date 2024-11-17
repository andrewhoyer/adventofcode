<?php

$filename   = $argv[1];
$handle     = fopen($filename, 'r');
$lines      = explode("\n", fread($handle, filesize($filename)));

fclose($handle);

$lights = [];

foreach ($lines as $line) {

    $parts = explode(' ', $line, strlen($line));

    // Pop the first element for "turn" instructions just to 
    // make every row have the same number of elements
    if ($parts[0] == "turn") {
        array_shift($parts);
    }

    $coords_start    = explode(',', $parts[1], strlen($parts[1]));
    $coords_end      = explode(',', $parts[3], strlen($parts[3]));

    for ($y = (int)$coords_start[1]; $y <= (int)$coords_end[1]; $y++) {
        for ($x = (int)$coords_start[0]; $x <= (int)$coords_end[0]; $x++) {

            if ($parts[0] == "on") {
                // Turn on a light
                $lights[$x . "-" . $y] = true;
            } elseif ($parts[0] == "off") {
                // Turn off a light
                unset($lights[$x . "-" . $y]);
            } else {
                // Toggle a light
                if (array_key_exists($x . "-" . $y, $lights)) {
                    unset($lights[$x . "-" . $y]);
                } else {
                    $lights[$x . "-" . $y] = true;
                }
            }

        }
    }

}

echo("The number of lights turned on: " . count($lights) . "\n");
