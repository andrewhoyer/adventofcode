<?php

$filename   = $argv[1];
$handle     = fopen($filename, 'r');
$data       = fread($handle, filesize($filename));

fclose($handle);

$houses = array();

$santa_x = 0;
$santa_y = 0;
$robot_x = 0;
$robot_y = 0;

// For Part 2, moves alternate between Santa and Robot
$santas_turn = true;

// Set the starting location
$houses["$santa_x-$santa_y"] = true;

for ($i = 0; $i < strlen($data); $i++) {

    if ($santas_turn) {
        if ($data[$i] == '^') {
            $santa_y++;
        } else if ($data[$i] == '>') {
            $santa_x++;
        } else if ($data[$i] == '<') {
            $santa_x--;
        } else if ($data[$i] == 'v') {
            $santa_y--;
        }

        $houses["$santa_x-$santa_y"] = true;
        $santas_turn = false;

    } else {
        if ($data[$i] == '^') {
            $robot_y++;
        } else if ($data[$i] == '>') {
            $robot_x++;
        } else if ($data[$i] == '<') {
            $robot_x--;
        } else if ($data[$i] == 'v') {
            $robot_y--;
        }

        $houses["$robot_x-$robot_y"] = true;
        $santas_turn = true;
    }

}

echo ("The number of houses visited: " . count($houses) . "\n");
