<?php

$filename   = $argv[1];
$handle     = fopen($filename, 'r');
$lines      = explode("\n", fread($handle, filesize($filename)));

fclose($handle);

$sum_part_1 = 0;

$antennas   = array();
$antinodes  = array();

$row_counter = 0;
foreach ($lines as $line) {

    for ($i = 0; $i < strlen($line); $i++) {

        if ($line[$i] != '.') {

            if (array_key_exists($line[$i], $antennas)) {

                // Do calculations on new antenna comparing with all existing ones of its type.
                find_antinodes(array($i, $row_counter), $antennas[$line[$i]]);

                // Add the antenna
                array_push($antennas[$line[$i]], array($i, $row_counter));

            } else {
                // Special case of creating the first antenna of its type
                $antennas[$line[$i]] = array(array($i, $row_counter));
            }

        }
    }

    $row_counter++;

}

echo "Solution for Part 2: " . count($antinodes) . "\n";

function find_antinodes($node, $antennas) {

    global $antinodes;
    global $lines;

    foreach ($antennas as $antenna) {

        // Determine the offset, which is used to check one direction, then
        // reversed to check the other.
        $offset_x = $antenna[0] - $node[0];
        $offset_y = $antenna[1] - $node[1];
            
        // Add new node location as an antinode (For Part 2 every antenna is also a node)
        create_antinode($node[0], $node[1]);


        // Check first direction

        $check_x = $node[0];
        $check_y = $node[1];

        while (true) {

            $check_x += $offset_x;
            $check_y += $offset_y;            

            if (! create_antinode($check_x, $check_y)) {
                break;
            }

        }

        // Check second direction

        $check_x = $node[0];
        $check_y = $node[1];

        $offset_x *= -1;
        $offset_y *= -1;

        while (true) {

            $check_x += $offset_x;
            $check_y += $offset_y;            

            if (! create_antinode($check_x, $check_y)) {
                break;
            }

        }
        
    }

}

function create_antinode($x, $y) {
    
    global $antinodes;
    global $lines;

    // Is the antinode in bounds?
    if ($x >= 0 && $x < strlen($lines[0]) && $y >= 0 && $y < count($lines)) {
        
        // Does it already exist?
        if (! in_array(array($x, $y), $antinodes)) {
            $antinodes[] = array($x, $y);
        }

        return true;

    } else {
        // Out of bounds
        return false;
    }

}
