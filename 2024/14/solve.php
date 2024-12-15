<?php

$filename   = $argv[1];
$handle     = fopen($filename, 'r');
$lines      = explode("\n", fread($handle, filesize($filename)));

fclose($handle);

$field_width_max = 100;
$field_height_max = 102;

// Set up all individual robot data
$robots = array();
foreach ($lines as $line) {

    $parts      = explode(" ", $line);
    $left       = explode("=", $parts[0]);
    $right      = explode("=", $parts[1]);
    $position   = explode(",", $left[1]);
    $velocity   = explode(",", $right[1]);

    $robots[] = array('pos' => [intval($position[0]),intval($position[1])], 'vel' => [intval($velocity[0]),intval($velocity[1])]);

}

// Calculate movement on robots for 100 seconds
for ($second = 1;$second <= 100;$second++) {

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
    
}

// Check each quadrant and calculate solution

$q1 = 0;
for ($x = 0;$x <= $field_width_max / 2 - 1;$x++) {
    for ($y = 0;$y <= $field_height_max / 2 - 1;$y++) {
        foreach ($robots as $robot) {
            if ($robot['pos'][0] == $x && $robot['pos'][1] == $y) {
                $q1++;
            }
        }
    }
}

$q2 = 0;
for ($x = $field_width_max / 2 + 1;$x <= $field_width_max;$x++) {
    for ($y = 0;$y <= $field_height_max / 2 - 1;$y++) {
        foreach ($robots as $robot) {
            if ($robot['pos'][0] == $x && $robot['pos'][1] == $y) {
                $q2++;
            }
        }
    }
}

$q3 = 0;
for ($x = 0;$x <= $field_width_max / 2 - 1;$x++) {
    for ($y = $field_height_max / 2 + 1;$y <= $field_height_max;$y++) {
        foreach ($robots as $robot) {
            if ($robot['pos'][0] == $x && $robot['pos'][1] == $y) {
                $q3++;
            }
        }
    }
}

$q4 = 0;
for ($x = $field_width_max / 2 + 1;$x <= $field_width_max;$x++) {
    for ($y = $field_height_max / 2 + 1;$y <= $field_height_max;$y++) {
        foreach ($robots as $robot) {
            if ($robot['pos'][0] == $x && $robot['pos'][1] == $y) {
                $q4++;
            }
        }
    }
}

echo "Solution for Part 1: " . $q1 * $q2 * $q3 * $q4 . "\n";
