<?php

$filename   = $argv[1];
$handle     = fopen($filename, 'r');
$lines      = explode("\n", fread($handle, filesize($filename)));

fclose($handle);

$sum_part_2 = 0;

foreach ($lines as $line) {

    $parts      = explode(": ", $line);
    $numbers    = explode(" ", $parts[1]);
    $first      = array_shift($numbers);
    
    if (next_value($first, "+", $numbers, intval($parts[0]), 0) == true ||
        next_value($first, "*", $numbers, intval($parts[0]), 0) == true ||
        next_value($first, "||", $numbers, intval($parts[0]), 0) == true
      ) {
        $sum_part_2 += intval($parts[0]);
    }

}

echo "Solution for Part 2: " . $sum_part_2 . "\n";

function next_value($first, $operator, $values, $target, $level) {

    $second = array_shift($values);

    $calculated = 0;
    if ($operator == "+") {
        $calculated = intval($first) + intval($second);
    } else if ($operator == "*") {
        $calculated = intval($first) * intval($second);
    } else if ($operator == "||") {
        $calculated = intval(strval($first) . strval($second));
    }

    if (count($values) > 0) {

        $level++;

        if (next_value($calculated, "+", $values, $target, $level) == true ||
            next_value($calculated, "*", $values, $target, $level) == true ||
            next_value($calculated, "||", $values, $target, $level) == true
            ) {
            return true;
        }

    } else {

        if ($calculated == $target) {
            return true;
        } else {
            return false;
        }
        
    }

}
