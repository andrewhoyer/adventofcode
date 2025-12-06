<?php

$filename   = $argv[1];
$handle     = fopen($filename, 'r');
$lines      = explode("\n", fread($handle, filesize($filename)));

fclose($handle);

// Set up grid array
$grid = []; // y,x

foreach ($lines as $line) {

    $chars  = str_split($line);
    $cols = [];

    foreach ($chars as $char) {
        $cols[] = $char;
    }

    $grid[] = $cols;

}

$total  = 0;
$remove = -1; // flag for existing loop, when it reaches 0

while ($remove != 0) {

    $removes    = [];
    $remove     = 0;

    $y = 0;

    foreach ($grid as $row) {

        $x = 0;

        foreach ($row as $col) {

            if ($grid[$y][$x] == "@") {        

                $count = 0;

                for ($y_check = -1;$y_check <= 1;$y_check++) {

                    // Avoid rows outside bounds
                    if ($y + $y_check < 0 || $y + $y_check > count($grid) - 1) {
                        continue;
                    }
                    
                    for ($x_check = -1;$x_check <= 1;$x_check++) {

                        // Avoid columns outside bounds
                        if ($x + $x_check < 0 || $x + $x_check > count($row) - 1) {
                            continue;
                        }

                        // Avoid the roll itself
                        if ($x_check == 0 && $y_check == 0) {
                            continue;
                        }

                        if ($grid[$y + $y_check][$x + $x_check] == "@") {
                            $count++;
                        }

                        

                    }        
                }

                if ($count < 4) {
                    $removes[] = [$y, $x];
                    $remove++;
                }
    
            }

            $x++;  

        }

        $y++;

    }

    $total += count($removes);

    // For each iteration, remove all accessible rolls
    foreach ($removes as $item) {
        $grid[$item[0]][$item[1]] = '.';
    }
    
}

print("Part 2 solution: " . $total . "\n");

exit();
