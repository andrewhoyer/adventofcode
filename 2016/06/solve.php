<?php

$visualize = false;

$filename   = $argv[1];
$handle     = fopen($filename, 'r');
$lines      = explode("\n", fread($handle, filesize($filename)));

fclose($handle);

$values = [];

// Build an array of dictionaries of the right size
foreach (str_split($lines[0]) as $char) {
    $values[] = [];
}

foreach ($lines as $line) {

    $counter = 0;
    foreach (str_split($line) as $char) {

        if (array_key_exists($char,$values[$counter])) {
            $values[$counter][$char]++;
        } else {
            $values[$counter][$char] = 1;
        }

        // Sort the associative array by value
        arsort($values[$counter]);

        $counter++;
    }

}

print("Part 1 Solution: ");

// Display first element of each associative array
foreach ($values as $value) {
    print(array_key_first($value));
}

print("\n");

print("Part 2 Solution: ");

// Display last element of each associative array
foreach ($values as $value) {
    print(array_key_last($value));
}

print("\n");

exit();
