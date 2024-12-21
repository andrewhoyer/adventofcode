<?php

$filename   = $argv[1];
$handle     = fopen($filename, 'r');
$file_parts = explode("\n\n", file_get_contents($filename));

fclose($handle);

$instructions = str_replace("\n", "", $file_parts[1]);

$rows   = array();
$x      = -1;
$y      = -1;

// Build the initial data set
$row_counter = 0;
foreach (explode("\n", $file_parts[0]) as $line) {

    $columns = array();
    for ($i = 0; $i < strlen($line); $i++) {

        if ($line[$i] == '@') {
            
            $columns[]  = '.';
            $x          = $i;
            $y          = $row_counter;
            
        } else {
            $columns[] = $line[$i];
        }

    }

    $rows[] = $columns;
    $row_counter++;
}

draw($rows);


$dir_x = 0;
$dir_y = 0;

for ($i = 0; $i < strlen($instructions); $i++) {
    
    if ($instructions[$i] == "^") {
        $dir_x = 0;
        $dir_y = -1;
    } else if ($instructions[$i] == "v") {
        $dir_x = 0;
        $dir_y = 1;
    } else if ($instructions[$i] == ">") {
        $dir_x = 1;
        $dir_y = 0;
    } else if ($instructions[$i] == "<") {
        $dir_x = -1;
        $dir_y = 0;
    }
    

    // If space is open, just move and continue to next step

    if ($rows[$y + $dir_y][$x + $dir_x] == ".") {

        $x += $dir_x;
        $y += $dir_y;

        draw($rows);
        continue;

    }

    // Search the grid in the moved direction, analyse, and push if possible.
    // If a # is reached at any time, continue to next step.

    $shift_blocks = array();
    $check_x = $x;
    $check_y = $y;

    while (true) {

        $check_x += $dir_x;
        $check_y += $dir_y;

        if ($rows[$check_y][$check_x] == ".") {
            // Found an empty space. This means that there's at least one 
            // box between robot and an empty space.

            // Shift all boxes in the correct direction.
            // Reversing the array is important to avoid overwriting each other.
            foreach (array_reverse($shift_blocks) as $block) {
                $rows[$block[1]][$block[0]] = ".";
                $rows[$block[1] + $dir_y][$block[0] + $dir_x] = "O";
            }

            // Move robot in the same direction.
            $x += $dir_x;
            $y += $dir_y;

            break;

        } else if ($rows[$check_y][$check_x] == "O") {

            // Found a box. Add it to the array and move on to see what
            // the next block contains.
            $shift_blocks[] = array($check_x, $check_y);

        } else if ($rows[$check_y][$check_x] == "#") {

            // Found a wall. Abandon any movement or checking.
            break;

        }

    }

    draw($rows);
    
}

$score = 0;

for ($y = 0; $y < count($rows); $y++) {
    for ($x = 0; $x < count($rows[$y]); $x++) {
        if ($rows[$y][$x] == "O") {
            $score += (100 * $y) + $x; 
        }
    }
}

echo "Solution for Part 1: " . $score . "\n";

// Visualiztion function
function draw($r) {
    
    // $r is kept as a param so its scope is limited to this
    // function because it gets modified with the robot's
    // location.

    global $x, $y;

    // Add the robot's location to the map
    $r[$y][$x] = "@";

    system('clear');

    $string = "";
    
    foreach ($r as $row) {
        foreach ($row as $column) {

            if ($column == "#") {
                $string .= "🟫";
            } else if ($column == "O") {
                $string .= "🎁";
            } else if ($column == ".") {
                $string .= "⬛️";
            } else {
                $string .= "🤖";
            }
            
        }

        $string .= "\n";

    }

    echo($string);
    usleep(200000); // microseconds

}