<?php

$filename   = $argv[1];
$handle     = fopen($filename, 'r');
$lines      = explode("\n", fread($handle, filesize($filename)));

fclose($handle);

$position       = 50;
$prev_position  = 50; // For P2. Helps detect when moving off of the 0 point.

$zeros_part1 = 0;
$zeros_part2 = 0;

foreach ($lines as $line) {
    
    $chars  = str_split($line); // Split into individual characters
    $dir    = array_shift($chars); // The direction, R or L
    $move   = intval(implode($chars)); // The rest of the line is a number

    // This may seem like an odd way to do this, but it leaves $char
    // with only values that are hundreds or thousands, making for quick
    // calculation for full rotations. See P2 note near the end.
    $last           = array_pop($chars);
    $second_last    = array_pop($chars);
    $move           = intval($second_last . $last);

    if ($dir == 'R') {
        
        $position = $position + intval($move);
        
        if ($position > 99) {
            $position = $position - 100;
            $zeros_part2++;
        } else if ($position == 0) {
            $zeros_part2++;
        }

    } else {
        
        $position = $position - intval($move);
        
        if ($position < 0) {
            $position = $position + 100;

            // For P2, when the previous position is 0, don't 
            // count an extra one.
            if ($prev_position != 0){
                $zeros_part2++;    
            }
        } else if ($position == 0) {
            $zeros_part2++;
        }

    }

    // P1. Add only when the end position is 0.
    if ($position == 0) {
        $zeros_part1++;
    }
    
    // P2. For the value over 99, just add that value to the count
    // since it's a full revolution. For example, R1456. Move right
    // 56, count a 0-click if needed, then add 14 because 1400 is
    // 14 full rotations.
    if (count($chars) > 0) {
        $zeros_part2 += intval(implode($chars));
    }

    // P2. See note above in the "L" section.
    $prev_position = $position;
}

print("Part 1 solution: " . $zeros_part1 . "\n");
print("Part 2 solution: " . $zeros_part2 . "\n");

exit();
