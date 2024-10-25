<?php

$filename   = 'data-input.txt';
$handle     = fopen($filename, 'r');
$lines      = explode("\n", fread($handle, filesize($filename)));

fclose($handle);

$total = 0;

foreach ($lines as $line) {
    $first  = '';
    $last   = '';

    for ($i = 0; $i < strlen($line); $i++) {
        if (is_numeric($line[$i])) {
            if ($first == '') {
                $first = $line[$i];
            } else {
                $last = $line[$i];
            }
        }
    }

    // In the unlikely event there's only a single number in the row, use it for both digits
    if ($last == '') {
        $last = $first;
    }
    
    $total += (int)($first . $last);

}

echo $total;
