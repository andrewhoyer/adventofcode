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

echo "Solution for Part 1: " . count($antinodes) . "\n";

function find_antinodes($node, $antennas) {

    global $antinodes;
    global $lines;

    foreach ($antennas as $antenna) {

        $antinode_1 = array(0,0);
        $antinode_2 = array(0,0);

        $offset_x = 0;
        $offset_y = 0;

        // Compare position of new and existing antenna and set values
        // for new antinodes accordingly.
        if ($node[0] > $antenna[0]) {
            $offset_x = $node[0] - $antenna[0];

            $antinode_1[0] = $node[0] + $offset_x;            
            $antinode_2[0] = $antenna[0] - $offset_x;
            
        } else if ($node[0] < $antenna[0]) {
            $offset_x = $antenna[0] - $node[0];
            
            $antinode_1[0] = $node[0] - $offset_x;
            $antinode_2[0] = $antenna[0] + $offset_x;
            
        } 

        if ($node[1] > $antenna[1]) {
            $offset_y = $node[1] - $antenna[1];
            
            $antinode_1[1] = $node[1] + $offset_y;
            $antinode_2[1] = $antenna[1] - $offset_y;
        } else if ($node[1] < $antenna[1]) {
            $offset_y = $antenna[1] - $node[1];

            $antinode_1[1] = $node[1] - $offset_y;
            $antinode_2[1] = $node[1] + $offset_y;
        } 
        
        // Ensure new antinodes are in bounds and not already antinodes
        if ($antinode_1[0] >= 0 && $antinode_1[0] < strlen($lines[0]) && $antinode_1[1] >= 0 && $antinode_1[1] < count($lines)) {
            if (! in_array(array($antinode_1[0], $antinode_1[1]), $antinodes)) {
                $antinodes[] = array($antinode_1[0], $antinode_1[1]);
            }
        }
        
        if ($antinode_2[0] >= 0 && $antinode_2[0] < strlen($lines[0]) && $antinode_2[1] >= 0 && $antinode_2[1] < count($lines)) {
            if (! in_array(array($antinode_2[0], $antinode_2[1]), $antinodes)) {
                $antinodes[] = array($antinode_2[0], $antinode_2[1]);
            }
        }

    }

}
