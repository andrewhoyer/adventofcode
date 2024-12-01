<?php

$filename   = $argv[1];
$handle     = fopen($filename, 'r');
$lines      = explode("\n", fread($handle, filesize($filename)));

fclose($handle);

$left   = array();
$right  = array();

foreach ($lines as $line) {

    $parts = explode("   ", $line);

    $left[]     = (int)$parts[0];
    $right[]    = (int)$parts[1];
    
}

sort($left);
sort($right);

$sum_part_1 = 0;
$sum_part_2 = 0;

for ($i = 0; $i < count($left); $i++) {

    if ($right[$i] > $left[$i]) {
        $sum_part_1 += $right[$i] - $left[$i];    
    } else {
        $sum_part_1 += $left[$i] - $right[$i];
    }

    $sum_part_2 += $left[$i] * count(array_keys($right, $left[$i]));

}

echo "Solution for Part 1: {$sum_part_1}\n";
echo "Solution for Part 2: {$sum_part_2}\n";
