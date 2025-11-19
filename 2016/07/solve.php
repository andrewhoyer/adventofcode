<?php

$visualize = false;

$filename   = $argv[1];
$handle     = fopen($filename, 'r');
$lines      = explode("\n", fread($handle, filesize($filename)));

fclose($handle);

$valid = [];

foreach ($lines as $line) {

    $flag = true;
    $palindrome_exists_once = false;

    $sections = preg_split("/[\[\]]/", $line);

    foreach ($sections as $section) {

        if (contains_palindrome($section) == true) {

            if ($flag == false) {
                // If a palindrome exists inside brackets, skip the entire line.
                continue 2;
            } else {
                // Set this flag, which we only need one of in all areas outside brackets
                $palindrome_exists_once = true;
            }
            
        }

        if ($flag == true) {
            $flag = false;
        } else {
            $flag = true;
        }

    }

    if ($palindrome_exists_once == true) {
        $valid[] = $line;
    }

}

print("Part 1 Solution: " . count($valid) . "\n");

exit();

function contains_palindrome($text) {

    $chars = str_split($text);

    for ($i = 0;$i <= strlen($text) - 4;$i++) {

        // Check for ABBA format
        if (
            $chars[$i] != $chars[$i + 1] &&
            $chars[$i] == $chars[$i + 3] &&
            $chars[$i + 1] == $chars[$i + 2]
            ) {

                return true;
            }

    }

    return false;

}
