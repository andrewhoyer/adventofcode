<?php

$filename   = $argv[1];
$handle     = fopen($filename, 'r');
$lines      = explode("\n", fread($handle, filesize($filename)));

fclose($handle);

// Create an array of all the data
$data = [];

foreach ($lines as $line) {

    $line = trim($line);

    $sides = preg_split("/\s+/", $line);
   
    $data[] = $sides;
    
}

// Work through the data in 3-line groups, iterating column by column,
// And for each of the three rows per group.

// The trick to part 2 is to sort the triangle sides after you have
// a group of three, not for each row as in part 1.

$counter = 0;
for ($i = 0;$i < count($lines);$i = $i + 3) {
    for ($col = 0;$col < 3;$col++) {
        $set = [];
        for ($row = 0;$row < 3;$row++) {    
            $set[] = intval($data[$i + $row][$col]);
        }
        sort($set);
        
        if ($set[0] + $set[1] > $set[2]) {
            $counter++;
        }
    }
}

print("Part 2 solution: " .$counter . "\n");

exit();
