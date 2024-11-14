<?php

$filename   = $argv[1];
$handle     = fopen($filename, 'r');
$data       = fread($handle, filesize($filename));

fclose($handle);

$counter            = 1;
$part_1_complete    = false;

while (true) {

    if (!$part_1_complete && substr(md5($data . $counter), 0, 5) === "00000") {
        echo("Part 1 solution. Value: " . $counter . " MD5: " . md5($data . $counter) . "\n");
        
        //  We only care about the first instance. Keep going, let part 2 finish.
        $part_1_complete = true;
    }

    if (substr(md5($data . $counter), 0, 6) === "000000") {
        echo("Part 2 solution. Value: " . $counter . " MD5: " . md5($data . $counter) . "\n");
        break;
    }

    $counter++;

}
