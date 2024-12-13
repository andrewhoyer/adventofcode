<?php

$filename   = $argv[1];
$handle     = fopen($filename, 'r');
$lines      = explode("\n", fread($handle, filesize($filename)));

fclose($handle);

// Part 1

$rows            = array();
$spaces_occupied = array();

$x          = -1;
$y          = -1;
$start_x    = -1;
$start_y    = -1;
$direction  = "up";


// Build the initial data set
$row_counter = 0;
foreach ($lines as $line) {

    $columns = array();
    for ($i = 0; $i < strlen($line); $i++) {

        if ($line[$i] == '^') {
            $columns[]  = '.';
            $x          = $i;
            $y          = $row_counter;
            $start_x    = $i;
            $start_y    = $row_counter;

            $spaces_occupied[$x . '|' . $x] = 1;
            
        } else {
            $columns[] = $line[$i];
        }
        

    }

    $rows[] = $columns;
    $row_counter++;
}

// The guard moves until such time as it leaves the field
while (true) {
    
    if ($direction == "up") {

        // First check if move is out of bounds.
        if ($y - 1 < 0) {
            break;
        }

        // Turn 90 degrees to the right when an obstacle is reached.
        if ($rows[$y-1][$x] == "#") {
            $direction = "right";

        } else {
            // Otherwise, move forward in current direction
            $y--;
            $spaces_occupied[$x . '|' . $y] = 1;

        }

    } else if ($direction == "down") {

        if ($y + 1 > count($rows) - 1) {
            break;
        }

        if ($rows[$y+1][$x] == "#") {
            $direction = "left";
        } else {
            $y++;
            $spaces_occupied[$x . '|' . $y] = 1;
        }

    } else if ($direction == "right") {

        if ($x + 1 > count($rows[0]) - 1) {
            break;
        }

        if ($rows[$y][$x+1] == "#") {
            $direction = "down";
        } else {
            $x++;
            $spaces_occupied[$x . '|' . $y] = 1;
        }

    } else if ($direction == "left") {

        if ($x - 1 < 0) {
            break;
        }

        if ($rows[$y][$x-1] == "#") {
            $direction = "up";
        } else {
            $x--;
            $spaces_occupied[$x . '|' . $y] = 1;
        }

    } 

}

echo "Solution for Part 1: " . count($spaces_occupied) . "\n";


// Part 2

// For this solution, the only places to be considered for placement
// of a new object is along the path the guard walks in part 1.
$possible_obstacle_positions = $spaces_occupied;

// Remove the starting position of the guard
unset($possible_obstacle_positions[$start_x . '|' . $start_y]);

$obstacles_to_force_loop = 0;

// Go through each possible obstacle position and test it
foreach (array_keys($possible_obstacle_positions) as $obstacle) {

    $row_counter    = 0;
    $x              = -1;
    $y              = -1;
    $direction      = "up";

    $spaces_occupied    = array();
    $rows               = array();

    foreach ($lines as $line) {

        $columns = array();
        for ($i = 0; $i < strlen($line); $i++) {
    
            if ($line[$i] == '^') {
                $columns[]  = '.';
                $x          = $i;
                $y          = $row_counter;

                $spaces_occupied[$x . '|' . $x] = 1;
                
            } else {
                $columns[]  = $line[$i];
            }
            
    
        }
    
        $rows[] = $columns;
        $row_counter++;
    }

    $sx_parts = explode('|', $obstacle);
    
    $rows[(int)$sx_parts[1]][(int)$sx_parts[0]] = "#";
    
    $loops_since_update = 0;

    while (true) {
        
        if ($direction == "up") {
    
            // First check if move is out of bounds.
            if ($y - 1 < 0) {
                break;
            }
            
            // Turn 90 degrees to the right when an obstacle is reached.
            if ($rows[$y-1][$x] == "#") {
                $direction = "right";
            } else {
    
                // Otherwise, move forward in current direction
                $y--;
                $spaces_occupied[$x . '|' . $y] = 1;
            }
    
        } else if ($direction == "down") {
            
            if ($y + 1 > count($rows) - 1) {
                break;
            }
    
            if ($rows[$y+1][$x] == "#") {
                $direction = "left";
            } else {
                $y++;
                $spaces_occupied[$x . '|' . $y] = 1;
            }
    
        } else if ($direction == "right") {

            if ($x + 1 > count($rows[0]) - 1) {
                break;
            }
    
            if ($rows[$y][$x+1] == "#") {
                $direction = "down";
            } else {
                $x++;
                $spaces_occupied[$x . '|' . $y] = 1;
            }
    
        } else if ($direction == "left") {
            
            if ($x - 1 < 0) {
                break;
            }
    
            if ($rows[$y][$x-1] == "#") {
                $direction = "up";
            } else {
                $x--;
                $spaces_occupied[$x . '|' . $y] = 1;
            }
    
        } 

        $loops_since_update++;

        // Abritrary number of steps to consider the loop infinite
        if ($loops_since_update > 100000) {
            $obstacles_to_force_loop++;
            break;
        }
    
    }

}

echo "Solution for Part 2: " . $obstacles_to_force_loop . "\n";
