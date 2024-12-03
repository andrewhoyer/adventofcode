<?php

$filename   = $argv[1];
$handle     = fopen($filename, 'r');
$lines      = explode("\n", fread($handle, filesize($filename)));

fclose($handle);

$total = 0;
$calculate = true;
foreach ($lines as $line) {

    preg_match_all("/mul\(\d{1,3},\d{1,3}\)|don't\(\)|do\(\)/", $line, $matches);
    
    foreach ($matches[0] as $match) {

        if ($match == "don't()") {
            $calculate = false;
            continue;
        } else if ($match == "do()") {
            $calculate = true;
            continue;
        }

        $match = str_replace('mul(', '', $match);
        $match = str_replace(')', '', $match);

        $parts = explode(',', $match);
        
        if ($calculate) {
            $total += (int)$parts[0] * (int)$parts[1];
        }

    }
}

echo "Solution for Part 2: {$total}\n";
