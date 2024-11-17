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
                // Increase brightness by 1
                if (array_key_exists($x . "-" . $y, $lights)) {
                    $lights[$x . "-" . $y] += 1;
                } else {
                    $lights[$x . "-" . $y] = 1;
                }
                
            } elseif ($parts[0] == "off") {
                // Decrease brightness by 1
                if (array_key_exists($x . "-" . $y, $lights)) {

                    // A trick! Don't let the brightness go below zero.
                    if ($lights[$x . "-" . $y] > 0) {
                        $lights[$x . "-" . $y] -= 1;
                    }

                } else {
                    $lights[$x . "-" . $y] = 0;
                }
                
            } else {
                // Increase brightness by 1
                if (array_key_exists($x . "-" . $y, $lights)) {
                    $lights[$x . "-" . $y] += 2;
                } else {
                    $lights[$x . "-" . $y] = 2;
                }

            }

        }
    }

}

// Calculate the total brightness
$brightness = 0;
foreach (array_keys($lights) as $key) {
    $brightness += $lights[$key];
}

echo("The total light brightness is: " . $brightness . "\n");
