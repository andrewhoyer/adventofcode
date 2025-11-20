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

    // Split intt arrays, one for sections outside brackets, and another for inside brackets.
    $outer = [];
    $inner = [];

    $counter = 0;
    foreach ($sections as $section) {

        if ($counter % 2 == 0) {
            $outer[] = $section;
        } else {
            $inner[] = $section;
        }

        $counter++;
    }

    // Find all ABA strings
    $abas = find_aba($outer);

    // Check all ABA strings against all inner sections for matches.
    foreach ($abas as $aba) {

        foreach ($inner as $inner_text) {
            
            if (str_contains($inner_text, $aba)) {
                $valid[] = $line;
                continue 3;
            }
        }
    }
}

print("Part 2 Solution: " . count($valid) . "\n");

exit();

function find_aba($texts) {

    $abas = [];

    foreach ($texts as $text) {

        $chars = str_split($text);

        for ($i = 0;$i <= strlen($text) - 3;$i++) {

            // Check for ABA format
            if ($chars[$i] != $chars[$i + 1] && $chars[$i] == $chars[$i + 2]) {
                    $abas[] = $chars[$i + 1] . $chars[$i] . $chars[$i + 1];
            }

        }
    }

    return $abas;

}
