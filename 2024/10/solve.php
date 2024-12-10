<?php

$filename   = $argv[1];
$handle     = fopen($filename, 'r');
$lines      = explode("\n", fread($handle, filesize($filename)));

fclose($handle);

// Part 2 of the puzzle is to find all unique trails
$distinct_trails = 0;

// Part 1 does not consider unique trails, but rather the number
// of summits a trailhead reaches.
$trail_score = array();

$row_count = 0;

foreach ($lines as $line) {

    for ($i = 0; $i < strlen($line); $i++) {
        if ($line[$i] == '.') {
            continue;
        }
        if (intval($line[$i]) == 0) {
            $distinct_trails += search_nearby($i, $row_count, 0, $i . "|" . strval($row_count));
        }

    }

    $row_count++;

}

echo "Solution for Part 1: " . count($trail_score) . "\n";
echo "Solution for Part 2: " . $distinct_trails . "\n";

function search_nearby($x, $y, $level, $origin) {
    global $lines;
    global $trail_score;

    /*
    // Debugging code
    $tab = '';
    for ($j=0;$j<=$level;$j++) {
        $tab .= '   ';
    }

    echo("$tab search $x, $y, height " . $lines[$y][$x] . " level $level, origin $origin\n");
    */

    // Return 1 as soon as the top level is reached.
    if ($level == 9) {

        // Set a key that is unique to the trailhead and the summit, for Part 1
        if (! array_key_exists("$origin - $x|$y", $trail_score)) {
            $trail_score["$origin - $x|$y"] = 1;
        }
        return 1;

    }

    $distinct_trails = 0;

    // Send off a recursive function call for each of the four directions if
    // there is space, and if it's the next level in the sequence.

    if ($x > 0) {
        if (intval($lines[$y][$x - 1]) == $level + 1) {
            $distinct_trails += search_nearby($x - 1, $y, $level + 1, $origin);
        } 
    }

    if ($x < strlen($lines[0]) - 1) {
        if (intval($lines[$y][$x + 1]) == $level + 1) {
            $distinct_trails += search_nearby($x + 1, $y, $level + 1, $origin);
        } 
    }

    if ($y > 0) {
        if (intval($lines[$y - 1][$x]) == $level + 1) {
            $distinct_trails += search_nearby($x, $y - 1, $level + 1, $origin);
        } 
    }

    if ($y < count($lines) - 1) {
        if (intval($lines[$y + 1][$x]) == $level + 1) {
            $distinct_trails += search_nearby($x, $y + 1, $level + 1, $origin);
        } 
    }

    return $distinct_trails;

}
