<?php

$filename   = $argv[1];
$handle     = fopen($filename, 'r');
$lines      = explode("\n", fread($handle, filesize($filename)));

fclose($handle);

$stones = explode(" ", $lines[0]);

for ($blink = 1;$blink <= 25;$blink++) {

    $i = 0;
    while ($i < count($stones)) {

        if ($stones[$i] == '0') {
            $stones[$i] = '1';
            $i++;
        } else if (strlen($stones[$i]) %2 == 0) {

            $first  = substr($stones[$i], 0, strlen($stones[$i]) / 2);
            $second = strval( intval( substr($stones[$i], strlen($stones[$i]) / 2, strlen($stones[$i]) / 2)));

            array_splice($stones, $i, 1, [$first, $second]);
            
            $i = $i + 2;

        } else {
            $stones[$i] = strval(intval($stones[$i]) * 2024);

            $i++;
        }

    }
    
		echo "Blink $blink, stone count: " . count($stones) . "\n";
}

echo "Solution for Part 1: " . count($stones) . "\n";

