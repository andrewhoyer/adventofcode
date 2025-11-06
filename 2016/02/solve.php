<?php

require_once('../../tools/php/class.split.php');

$filename   = $argv[1];
$handle     = fopen($filename, 'r');
$lines      = explode("\n", fread($handle, filesize($filename)));
array_pop($lines); // Remove last blank entry.

fclose($handle);

// Text splitter
$splitter = new Splitter;

// Part 1
$keypad  = [
    ['1','2','3'],
    ['4','5','6'],
    ['7','8','9']
];

// Start off at the 5 position.
$pos = [1,1];
$password = '';

// Part 2
$keypad2 = [
    ['.', '.', '1', '.', '.'],
    ['.', '2', '3', '4', '.'],
    ['5', '6', '7', '8', '9'],
    ['.', 'A', 'B', 'C', '.'],
    ['.', '.', 'D', '.', '.']
];

// Start off at the 5 position.
$pos2 = [0,2];
$password2 = '';

foreach ($lines as $line) {
    
    // Iterate, adjusting the position, and recording the final value for each line.
    foreach ($splitter->str_to_array($line) as $dir) {

        // Part 1 and 2 are evaluated for each case.
        if ($dir == 'U') {
            if ($pos[1] > 0) {
                $pos[1]--;
            }
            if ($pos2[1] > 0 && $keypad2[$pos2[1] - 1][$pos2[0]] != '.') {
                $pos2[1]--;
            }
        } elseif ($dir == 'D') {
            if ($pos[1] < 2) {
                $pos[1]++;
            }
            if ($pos2[1] < 4 && $keypad2[$pos2[1] + 1][$pos2[0]] != '.') {
                $pos2[1]++;
            }
        } elseif ($dir == 'L') {
            if ($pos[0] > 0) {
                $pos[0]--;
            }
            if ($pos2[0] > 0 && $keypad2[$pos2[1]][$pos2[0] - 1] != '.') {
                $pos2[0]--;
            }
        } elseif ($dir == 'R') {
            if ($pos[0] < 2) {
                $pos[0]++;
            }
            if ($pos2[0] < 4 && $keypad2[$pos2[1]][$pos2[0] + 1] != '.') {
                $pos2[0]++;
            }
        }

        // Use this to display a visualization.
        //draw();
    }

    $password  .= $keypad[$pos[1]][$pos[0]];
    $password2 .= $keypad2[$pos2[1]][$pos2[0]];  
    
}

print("Part 1 solution: " .$password . "\n");
print("Part 2 solution: " .$password2 . "\n");

exit();


// Visualiztion function
function draw() {

    global $pos, $keypad;
    global $pos2, $keypad2;

    system('clear');

    // Loop the 3x3 grid and display.
    for ($y = 0;$y <= 2; $y++) {
        for ($x = 0;$x <= 2; $x++) {
            if ($x == $pos[0] && $y == $pos[1]) {
                print('▓');
            } else {
                print($keypad[$y][$x]);
            }
        }
        print("\n");
    }

    // Loop the 5x5 grid and display.
    for ($y = 0;$y <= 4; $y++) {
        for ($x = 0;$x <= 4; $x++) {
            if ($x == $pos2[0] && $y == $pos2[1]) {
                print('▓');
            } else {
                print($keypad2[$y][$x]);
            }
        }
        print("\n");
    }

    usleep(100000); // microseconds

}
