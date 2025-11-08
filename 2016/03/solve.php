<?php

$filename   = $argv[1];
$handle     = fopen($filename, 'r');
$lines      = explode("\n", fread($handle, filesize($filename)));

fclose($handle);

$counter = 0;

foreach ($lines as $line) {

    $line = trim($line);

    $sides = preg_split("/\s+/", $line);

    sort($sides);
   
    if (intval($sides[0]) + intval($sides[1]) > intval($sides[2])) {
        $counter++;
    }
    
}

print("Part 1 solution: " .$counter . "\n");

exit();
