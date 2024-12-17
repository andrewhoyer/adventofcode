<?php

$filename   = $argv[1];
$handle     = fopen($filename, 'r');
$file_parts = explode("\n\n", file_get_contents($filename));

fclose($handle);

$section1   = explode("\n", $file_parts[0]);
$registers  = array(
    0,
    1,
    2,
    3,
    intval(explode(": ",$section1[0])[1]),
    intval(explode(": ",$section1[1])[1]),
    intval(explode(": ",$section1[2])[1]),
    0
);

$program = explode(",", explode(": ", $file_parts[1])[1]);

$counter = 0;
$outputs = array();

while ($counter < count($program)) {

    // Terminate program if there aren't enough instructions left
    if ($counter > count($program) - 2) {
        break;
    }

    $operand    = intval($program[$counter]);
    $combo      = intval($program[$counter + 1]);

    if ($operand == 0) {
        $registers[4] = intval($registers[4] / (2 ** $registers[$combo]));
    } else if ($operand == 1) {
        $registers[5] = $registers[5] ^ $combo;
    } else if ($operand == 2) {
        $registers[5] = $registers[$combo] % 8;
    } else if ($operand == 3) {
        
        // If Register 4 is not zero, move the program pointer
        // and do not adjust the pointer by 2 as usual.
        if ($registers[4] != 0) {
            $counter = $combo;
            continue;
        }        
        
    } else if ($operand == 4) {
        $registers[5] = $registers[5] ^ $registers[6];
    } else if ($operand == 5) {
        // The output
        $outputs[] = $registers[$combo] % 8;
    } else if ($operand == 6) {
        $registers[5] = intval($registers[4] / (2 ** $registers[$combo]));
    } else if ($operand == 7) {
        $registers[6] = intval($registers[4] / (2 ** $registers[$combo]));
    }

    // Move the program instruction pointer forward.
    $counter += 2;
    
}

echo("Output for Part 1: " . join(",", $outputs) . "\n");
