<?php

$filename   = $argv[1];
$handle     = fopen($filename, 'r');
$lines      = explode("\n", fread($handle, filesize($filename)));

fclose($handle);

$total = 0;
foreach ($lines as $line) {

    preg_match_all('/mul\(\d{1,3},\d{1,3}\)/', $line, $matches);

    foreach ($matches[0] as $match) {
        
        $match = str_replace('mul(', '', $match);
        $match = str_replace(')', '', $match);

        $parts = explode(',', $match);
        
        $total += (int)$parts[0] * (int)$parts[1];

    }

}

echo "Solution for Part 1: {$total}\n";
