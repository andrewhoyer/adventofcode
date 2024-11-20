<?php

$filename   = $argv[1];
$handle     = fopen($filename, 'r');
$lines      = explode("\n", fread($handle, filesize($filename)));

fclose($handle);

$total_string           = 0;
$total_memory           = 0;
$total_slashed_string   = 0; // Part 2

foreach ($lines as $line) {

    // Part 1
    $total_string += strlen($line);

    // Part 2
    $total_slashed_string += strlen(addslashes($line)) + 2;

    // Replace hex characters
    $pattern = '/\\\\x([0-9A-Fa-f]{2})/';
    $line = preg_replace_callback($pattern, function($matches) {
        // Converts the hex value to a decimal value, and then to the character itself.
        return chr(hexdec($matches[1]));    
    }, $line);

    // Replace escaped double quotes
    $pattern = '/\\\"/';
    $replacement = '"';
    $line = preg_replace($pattern, $replacement, $line);
    
    // Replace double backslashes
    $pattern = '/\\\{2}/';
    $replacement = '\\';
    $line = preg_replace($pattern, $replacement, $line);
    
    $total_memory += strlen($line) - 2;
    
}

echo("Difference (Part 1) between string length and memory length: " . $total_string - $total_memory . "\n");
echo("Difference (Part 2) between escaped new string vs original: " . $total_slashed_string - $total_string . "\n");
