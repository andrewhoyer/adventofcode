<?php

$filename   = $argv[1];
$handle     = fopen($filename, 'r');
$lines      = explode("\n", fread($handle, filesize($filename)));

fclose($handle);

// Define field robots can move within
$field_width_max    = 100;
$field_height_max   = 102;

$robots = array();

foreach ($lines as $line) {

    $parts      = explode(" ", $line);
    $left       = explode("=", $parts[0]);
    $right      = explode("=", $parts[1]);
    $position   = explode(",", $left[1]);
    $velocity   = explode(",", $right[1]);

    $robots[] = array('pos' => [intval($position[0]),intval($position[1])], 'vel' => [intval($velocity[0]),intval($velocity[1])]);

}

$second = 0;
while (true) {

    $second++;

    foreach ($robots as &$robot) {

        $robot['pos'][0] += $robot['vel'][0];
        $robot['pos'][1] += $robot['vel'][1];
        
        if ($robot['pos'][0] < 0) {
            $robot['pos'][0] += $field_width_max + 1;
        } else if ($robot['pos'][0] > $field_width_max) {
            $robot['pos'][0] -= $field_width_max + 1;
        }

        if ($robot['pos'][1] < 0) {
            $robot['pos'][1] += $field_height_max + 1;
        } else if ($robot['pos'][1] > $field_height_max) {
            $robot['pos'][1] -= $field_height_max + 1;
        }

    }
    unset($robot);

    // After each "second", look for a row of sequential robots.
    // 10 is chosen as an arbitrary number, which found the
    // correct frame on the first try.

    $sequential_count = 0;
    
    for ($y = 0;$y <= $field_height_max;$y++) {

        $sequential_count = 0;
        for ($x = 0;$x <= $field_width_max;$x++) {

            $found_x = false;
            foreach ($robots as $robot) {
                if ($robot['pos'][0] == $x && $robot['pos'][1] == $y) {
                    $found_x = true;
                    break;
                }
            }

            if ($found_x == true) {
                $sequential_count++;
            } else {
                $sequential_count = 0;
            }

            if ($sequential_count >= 10) {
                break 2;
            }

        }
    }

    //system('clear');
    for ($y = 0;$y <= $field_height_max;$y++) {
        for ($x = 0;$x <= $field_width_max;$x++) {  

            $occupied = false;
            foreach ($robots as $robot) {
                if ($robot['pos'][0] == $x && $robot['pos'][1] == $y) {
                    $occupied = true;
                    break;
                }
            }
            /*
            if ($occupied == true) {
                echo "*";
            } else {
                echo " ";
            }
            */
        }

        //echo("\n");

    }

    if ($sequential_count >= 10) {
        break;
    }

}

echo "Solution for Part 2: $second\n";
