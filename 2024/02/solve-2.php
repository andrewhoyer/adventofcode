<?php

$filename   = $argv[1];
$handle     = fopen($filename, 'r');
$lines      = explode("\n", fread($handle, filesize($filename)));

fclose($handle);

$safe = 0;

foreach ($lines as $line) {
    
    $parts = explode(" ", $line);

    // Part 2 allows for one "bad" item per list. This method is a 
    // bit on the brute force side of things, but it works. One by
    // one, process each list after removing each item in turn.

    for ($j = 0; $j < count($parts); $j++) {

        $temp = $parts;

        // Remove a single element from the array
        array_splice($temp, $j, 1);

        $previous = 0;

        // Check ascending

        $asc_check = true;
        for ($i = 0; $i < count($temp); $i++) {

            if ($i == 0) {
                $previous = $temp[0];
                continue;
            }

            if ((int)$temp[$i] < (int)$previous) {
                $asc_check = false;
                continue;
            }

            $previous = $temp[$i];

        }

        // Check decending

        $dec_check = true;
        for ($i = 0; $i < count($temp); $i++) {

            if ($i == 0) {
                $previous = $temp[0];
                continue;
            }

            if ((int)$temp[$i] > (int)$previous) {
                $dec_check = false;
                continue;
            }

            $previous = $temp[$i];

        }
        
        // Check variance

        $var_check = true;
        for ($i = 0; $i < count($temp); $i++) {

            if ($i == 0) {
                $previous = $temp[0];
                continue;
            }

            if (abs((int)$temp[$i] - (int)$previous ) < 1 || abs((int)$temp[$i] - (int)$previous ) > 3) {
                $var_check = false;
                break;
            }

            $previous = $temp[$i];

        }

        // Logic check. The list must be either ascending or descending
        // and must not have variance less than 1 or greater than 3.
        if (($asc_check || $dec_check) && $var_check) {
            $safe++;
            break;
        }

    }
}

echo "Solution for Part 2: {$safe}\n";
