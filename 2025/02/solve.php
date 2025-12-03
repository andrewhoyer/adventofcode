<?php

$filename   = $argv[1];
$handle     = fopen($filename, 'r');
$lines      = explode("\n", fread($handle, filesize($filename)));

fclose($handle);

$sum_1 = 0;
$sum_2 = 0;

$ranges = explode(",", trim($lines[0]));

foreach ($ranges as $range) {

    $ids = explode("-", $range);

    // Uneven string on both sides, skip
    if (strlen($ids[0]) % 2 == 1 && strlen($ids[0]) == strlen($ids[1])) {
        continue;
    }

    // Loop throught all values.
    for ($i = intval($ids[0]);$i <= intval($ids[1]);$i++) {

        $text_i = strval($i); // Treating the number as a string.
        
        if (strlen($text_i) % 2 == 1 ) {
            continue;
        }

        if (substr($text_i, 0, strlen($text_i) / 2) == substr($text_i, strlen($text_i) / 2, strlen($text_i) / 2)) {
            // First half matches the last half
            $sum_1 += $i;
        }
    }
}

print("Part 1 solution: " . $sum_1 . "\n");


// PART 2

foreach ($ranges as $range) {

    $ids = explode("-", $range);

    for ($i = intval($ids[0]);$i <= intval($ids[1]);$i++) {

        $text_i     = strval($i);
        $text_len   = strlen($text_i);
        $midpoint   = floor($text_len / 2); // The rounded down middle point of the string.

        // Start comparing 1 character, then 2, and on up to the halfway point.
        for ($j = 1;$j <= $compare_start; $j += 1) {

            // If the full number can be divided evenly into segments, proceed.
            if ($text_len % $j == 0) {
                
                $segments = str_split($text_i, $j);
                
                $same = true;
                foreach ($segments as $segment) {
                    if ($segment === $segments[0]) {
                        continue;
                    } else {
                        $same = false;
                        break;
                    }
                }

                // If all compared segments match, add and move on.
                if ($same) {
                    $sum_2 += $i;
                    break;
                }
            } 
        }
    }
}

print("Part 2 solution: " . $sum_2 . "\n");

exit();
