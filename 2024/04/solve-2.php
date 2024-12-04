<?php

$filename   = $argv[1];
$handle     = fopen($filename, 'r');
$lines      = explode("\n", fread($handle, filesize($filename)));

fclose($handle);

$xmas_count = 0;
$row_count = 0;
foreach ($lines as $line) {

    for ($i = 0; $i < strlen($line); $i++) {

        if ($line[$i] == "A") {
            $xmas_count += search_xmas($i, $row_count, $lines);
        }

    }

    $row_count++;

}

echo "Solution for Part 2: {$xmas_count}\n";

function search_xmas($x, $y, $lines) {

    $count = 0;

    if ($x > 0 && $x < strlen($lines[0]) - 1 && $y > 0 && $y < count($lines) - 1) {
        
        $count += check_grid($x, $y, $lines);

    }

    return $count;

}

function check_grid($x, $y, $lines) {
    
    // Down
    if ( $lines[$y-1][$x-1] == "M" && $lines[$y-1][$x+1] == "M" && $lines[$y+1][$x-1] == "S" && $lines[$y+1][$x+1] == "S" ) {
        return 1;
    // Up
    } else if ( $lines[$y+1][$x-1] == "M" && $lines[$y+1][$x+1] == "M" && $lines[$y-1][$x-1] == "S" && $lines[$y-1][$x+1] == "S" ) {
        return 1;
    // Right
    } else if ( $lines[$y-1][$x-1] == "M" && $lines[$y+1][$x-1] == "M" && $lines[$y-1][$x+1] == "S" && $lines[$y+1][$x+1] == "S" ) {
        return 1;
    // Left
    } else if ( $lines[$y-1][$x+1] == "M" && $lines[$y+1][$x+1] == "M" && $lines[$y-1][$x-1] == "S" && $lines[$y+1][$x-1] == "S" ) {
        return 1;
    } else {
        return 0;
    }

}
