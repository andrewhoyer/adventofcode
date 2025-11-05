<?php

require_once('../../tools/php/class.split.php');
require_once('../../tools/php/class.output.grid.php');

$filename   = $argv[1];
$handle     = fopen($filename, 'r');
$lines      = explode("\n", fread($handle, filesize($filename)));

fclose($handle);

// Split each move into a usable array
$splitter = new Splitter;
$moves = $splitter->split_text($lines[0], ', ');

$pos = [0,0];
$dir = 0;

// Part 2
$path = [];
$part2 = -1; // Distance is absolute, so answer will be 0 or higher

foreach ($moves as $move) {

    if (substr($move, 0, 1) == 'R') {
        $dir++;
        if ($dir > 3) {
            $dir = 0;
        }
    } else {
        $dir--;
        if ($dir < 0) {
            $dir = 3;
        }
    }

    $i = 1;

    while ($i <= intval(substr($move, 1))) {
        if ($dir == 0) {
            $pos[1] = $pos[1] + 1;
        } elseif ($dir == 1) {
            $pos[0] = $pos[0] + 1;
        } elseif ($dir == 2) {
            $pos[1] = $pos[1] - 1;
        } elseif ($dir == 3) {
            $pos[0] = $pos[0] - 1;
        }

        $grid_text = '🟥';

        // Find the first instance the path overlaps
        if ($part2 == -1 && array_key_exists($pos[0]. ',' . $pos[1], $path)) {
            $part2 = abs($pos[0]) + abs($pos[1]);
            $grid_text = '🟩';
        }

        $path[$pos[0]. ',' . $pos[1]] = $grid_text;

        $i++;
    }

}

// Use this to output a visual grid. Write it to a file:
// $ php solve.php data-input.txt > grid.txt
//$output = new OutputGrid;
//$output->output_grid($path);

// The solution to both part 1 and 2 is the distance, x + y from 0, 0.
echo("Part 1 solution: " . abs($pos[0]) + abs($pos[1]) . "\n");
echo("Part 2 solution: " . $part2 . "\n");

exit();
