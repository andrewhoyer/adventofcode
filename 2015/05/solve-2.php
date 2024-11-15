<?php

$filename   = $argv[1];
$handle     = fopen($filename, 'r');
$lines      = explode("\n", fread($handle, filesize($filename)));

fclose($handle);

$counter = 0;

foreach ($lines as $line) {
    
    $matching_text      = false;
    $duplicate_letter   = false;
    $last_letter        = '';

    for ($i = 0; $i < strlen($line); $i++) {
        
        // For every two character segment, search for it only
        // in the rest of the string that follows
        if (str_contains( substr($line, $i + 2), substr($line, $i, 2) ) ) {
            $matching_text = true;
        }

        // Start comparing at the 3rd character to avoid
        // checking elements less than 0
        if ($i >= 2) {
            if ($line[$i - 2] == $line[$i]) {
                $duplicate_letter = true;
            }
        }
        
    }

    if ($matching_text && $duplicate_letter) {
        $counter++;
    }

}

echo("Total nice strings: " . $counter . "\n");
