<?php

$filename   = $argv[1];
$handle     = fopen($filename, 'r');
$lines      = explode("\n", fread($handle, filesize($filename)));

fclose($handle);

$text_numbers = array(
    'one' => 1,
    'two' => 2,
    'three' => 3,
    'four' => 4,
    'five' => 5,
    'six' => 6,
    'seven' => 7,
    'eight' => 8,
    'nine' => 9
);

$result_part_1 = 0;
$result_part_2 = 0;

foreach ($lines as $line) {

    // For the benefit of Part 2, the default first and last positions are 
    // set to be on the extreme oppsite ends. It's especially important for cases 
    // where no numbers appear in a row.
    $first      = '';
    $last       = '';
    $first_pos  = strlen($line);
    $last_pos   = -1;

    for ($i = 0; $i < strlen($line); $i++) {
        if (is_numeric($line[$i])) {
            if ($first == '') {
                $first      = $line[$i];
                $first_pos  = $i;
            } else {
                $last       = $line[$i];
                $last_pos   = $i;
            }
        }
    }

    // For Part 1, if no numbers are found, we have to skip the calculation on that row
    if ($first != '') {
        
        // In the event there's only a single number in the row, use it for both digits
        if ($last == '') {
            $last       = $first;
            $last_pos   = $first_pos;
        }
    
        // Calculate result for part 1 using just the numbers found in the string
        $result_part_1 += (int)($first . $last);
    }

    // Part 2
    // Search for each number word and update the first and last values if the word
    // appears before or after the latest known first or last position.
    foreach (array_keys($text_numbers) as $key) {

        // Search from the start of the line
        $position = strpos($line, $key);

        if ($position === false) {
            // Do nothing
        } else {
            if ($position < $first_pos) {
                $first      = $text_numbers[$key];
                $first_pos  = $position;
            }
        }

        // Search from the end of the line
        $position = strrpos($line, $key);

        if ($position === false) {
            // Do nothing
        } else {
            if ($position > $last_pos) {
                $last      = $text_numbers[$key];
                $last_pos  = $position;
            }
        }        
        
    }

    $result_part_2 += (int)($first . $last);

}

echo "Solution for Part 1: {$result_part_1}\n";
echo "Solution for Part 2: {$result_part_2}\n";
