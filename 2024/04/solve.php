<?php

$filename   = $argv[1];
$handle     = fopen($filename, 'r');
$lines      = explode("\n", fread($handle, filesize($filename)));

fclose($handle);

$xmas_count = 0;
$row_count = 0;
foreach ($lines as $line) {

    for ($i = 0; $i < strlen($line); $i++) {

        if ($line[$i] == "X") {
            $xmas_count += search_xmas($i, $row_count, $lines);
        }

    }

    $row_count++;

}

echo "Solution for Part 1: {$xmas_count}\n";

function search_xmas($x, $y, $lines) {
    $count = 0;

    if ($x > 2) {
        // Left
        $count += check_grid($x, $y, -1, 0, $lines, "LEFT");

        // Left Up
        if ($y > 2) {
            $count += check_grid($x, $y, -1, -1, $lines, "LEFT UP");
        }

        // Left Down
        if ($y < count($lines) - 3) {
            $count += check_grid($x, $y, -1, 1, $lines, "LEFT DOWN");
        }
    }

    if ($x < strlen($lines[0]) - 3) {
        // Right
        $count += check_grid($x, $y, 1, 0, $lines, "RIGHT");

        // Right Up
        if ($y > 2) {
            $count += check_grid($x, $y, 1, -1, $lines, "RIGHT UP");
        }

        // Right Down
        if ($y < count($lines) - 3) {
            $count += check_grid($x, $y, 1, 1, $lines, "RIGHT DOWN");
        }
    }

    // Up
    if ($y > 2) {
        $count += check_grid($x, $y, 0, -1, $lines, "UP");
    }

    // Down
    if ($y < count($lines) - 3) {
        $count += check_grid($x, $y, 0, 1, $lines, "DOWN");
    }

    return $count;

}

function check_grid($x, $y, $dir_x, $dir_y, $lines, $direction) {
    if ( $lines[$y + $dir_y][$x + $dir_x]           == "M" && 
         $lines[$y + $dir_y * 2][$x + $dir_x * 2]   == "A" && 
         $lines[$y + $dir_y * 3][$x + $dir_x * 3]   == "S" ) {
        
        return 1;

    } else {
        return 0;
    }
}
