<?php

$filename   = $argv[1];
$handle     = fopen($filename, 'r');
$lines      = explode("\n", fread($handle, filesize($filename)));

fclose($handle);

$counter = 0;

foreach ($lines as $line) {
    
    if (str_contains($line, "ab") || str_contains($line, "cd") || str_contains($line, "pq") || str_contains($line, "xy")) {
        continue;
    }

    $vowel_count        = 0;
    $duplicate_letter   = false;
    $last_letter        = '';

    for ($i = 0; $i < strlen($line); $i++) {

        if (in_array($line[$i], ['a','e','i','o','u'] ) ) {
            $vowel_count++;
        }

        if ($line[$i] == $last_letter) {
            $duplicate_letter = true;
        }

        $last_letter = $line[$i];

    }

    if ($vowel_count < 3 || !$duplicate_letter) {
        continue;
    }

    $counter++;
}

echo("Nice strings: " . $counter . "\n");
