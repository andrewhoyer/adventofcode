<?php

require_once('../../tools/php/class.split.php');

$filename   = $argv[1];
$handle     = fopen($filename, 'r');
$lines      = explode("\n", fread($handle, filesize($filename)));
array_pop($lines); // Remove last blank entry.

fclose($handle);

// Text splitter
$splitter = new Splitter;

$keypad = [['1️⃣','2️⃣','3️⃣'],['4️⃣','5️⃣','6️⃣'],['7️⃣','8️⃣','9️⃣']];

// Start off at the 5 position.
// 123
// 456
// 789
$pos = [1,1];

$password = '';

foreach ($lines as $line) {
    
    // Iterate, adjusting the position, and recording the final value for each line.
    foreach ($splitter->str_to_array($line) as $dir) {
        if ($dir == 'U') {
            if ($pos[1] > 0) {
                $pos[1]--;
            }
        } elseif ($dir == 'D') {
            if ($pos[1] < 2) {
                $pos[1]++;
            }
        } elseif ($dir == 'L') {
            if ($pos[0] > 0) {
                $pos[0]--;
            }
        } elseif ($dir == 'R') {
            if ($pos[0] < 2) {
                $pos[0]++;
            }
        }

        // Use this to display a visualization.
        //draw();
    }

    $password .= $keypad[$pos[1]][$pos[0]];  
    
}

print("Part 1 solution: " .$password . "\n");

exit();


// Visualiztion function
function draw() {

    global $pos, $keypad;

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

    usleep(100000); // microseconds

}
