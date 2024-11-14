<?php

$filename   = $argv[1];
$handle     = fopen($filename, 'r');
$data       = fread($handle, filesize($filename));

fclose($handle);

$houses = array();

$x = 0;
$y = 0;

// Set the starting location
$houses["$x-$y"] = true;

for ($i = 0; $i < strlen($data); $i++) {

    if ($data[$i] == '^') {
        $y++;
    } else if ($data[$i] == '>') {
        $x++;
    } else if ($data[$i] == '<') {
        $x--;
    } else if ($data[$i] == 'v') {
        $y--;
    }

    $houses["$x-$y"] = true;

}

echo ("The number of houses visited: " . count($houses) . "\n");
