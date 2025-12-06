<?php

$filename   = $argv[1];
$handle     = fopen($filename, 'r');
$lines      = explode("\n", fread($handle, filesize($filename)));

fclose($handle);

$total = 0;

foreach ($lines as $line) {
    
    $high = [0,0];

    $chars  = str_split($line);

    while (count($chars) > 0) {
        $next = intval(array_shift($chars));

        // If the number is higher than the second digit, place it there.
        if ($next > $high[1]) {
            array_pop($high);
            $high[] = $next;

            // If it's not the last element, and the number is higher than the 
            // first digit, move it to the first spot.
            if (count($chars) != 0) {
                if ($high[1] > $high[0]) {
                    array_shift($high);
                    $high[] = 0;
                }
            }
        }
    }

    $total += intval($high[0] . $high[1]);

}

print("Part 1 solution: " . $total . "\n\n");

// Part 2

$total = 0;

foreach ($lines as $line) {

    $highest        = [];
    $chars          = str_split($line);
    $complete       = false;
    $digits_needed  = 12;
    $pointer_main   = 0;
    $high_position  = 0;

    while (! $complete) {

        if ($digits_needed <= 0) {
            break;
        }

        $high_value = 0;
        
        for ($i = $pointer_main;$i <= ((count($chars) - 1) - $digits_needed + 1);$i++ ) {
            
            if ( intval($chars[$i]) > $high_value ) {
                $high_value = $chars[$i];
                $high_position = $i;
            }
        }
        
        $highest[] = $high_value;
        $pointer_main = $high_position + 1;

        $digits_needed--;

    }

    $total += intval(implode('', $highest));

}

print("Part 2 solution: " . $total . "\n");

exit();
