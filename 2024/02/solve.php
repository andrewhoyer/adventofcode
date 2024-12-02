<?php

$filename   = $argv[1];
$handle     = fopen($filename, 'r');
$lines      = explode("\n", fread($handle, filesize($filename)));

fclose($handle);

$safe = 0;

foreach ($lines as $line) {

    $parts = explode(" ", $line);
    
    $previous = 0;

    // Check Ascending

    $asc_check = true;
    for ($i = 0; $i < count($parts); $i++) {

        if ($i == 0) {
            $previous = $parts[0];
            continue;
        }

        if ((int)$parts[$i] < (int)$previous) {
            $asc_check = false;
            break;
        }

        $previous = $parts[$i];

    }
    
    // Check Decending

    $dec_check = true;
    for ($i = 0; $i < count($parts); $i++) {

        if ($i == 0) {
            $previous = $parts[0];
            continue;
        }

        if ((int)$parts[$i] > (int)$previous) {
            $dec_check = false;
            break;
        }

        $previous = $parts[$i];

    }
    
    // Check variance between numbers

    $var_check = true;
    for ($i = 0; $i < count($parts); $i++) {

        if ($i == 0) {
            $previous = $parts[0];
            continue;
        }

        if (abs((int)$parts[$i] - (int)$previous ) < 1 || abs((int)$parts[$i] - (int)$previous ) > 3) {
            $var_check = false;
            break;
        }

        $previous = $parts[$i];
    }

    // Logic check. The list must be either ascending or descending
    // and must not have variance less than 1 or greater than 3.
    if (($asc_check || $dec_check) && $var_check) {
        $safe++;
        continue;
    }
    
}

echo "Solution for Part 1: {$safe}\n";
