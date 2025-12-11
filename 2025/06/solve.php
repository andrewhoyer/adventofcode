<?php

$filename   = $argv[1];
$handle     = fopen($filename, 'r');
$lines      = explode("\n", fread($handle, filesize($filename)));

fclose($handle);

// Build the array of values.
$values = [];

foreach ($lines as $line) {

    $line = trim($line);

    $vals = preg_split("/\s+/",$line);

    $values[] = $vals;

}

// Loop through every column, taking the necessary math action.
$total = 0;
for ($i = 0;$i <= count($values[0]) - 1; $i++) {
    
    $subtotal = 0;

    for ($j = 0;$j < count($values) - 1; $j++) {
        
        if ($values[count($values) - 1][$i] == '+') {
            $subtotal += intval($values[$j][$i]);
        } else if ($values[count($values) - 1][$i] == '*') {
            
            // A trick! If substotal is zero, multiplying by it will result in 0
            if ($subtotal == 0) $subtotal = 1;

            $subtotal *= intval($values[$j][$i]);
        }

    }

    $total += $subtotal;

}

print("Part 1 solution: " . $total . "\n");

exit();
