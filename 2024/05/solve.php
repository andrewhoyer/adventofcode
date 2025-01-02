<?php

$filename   = $argv[1];

$file_parts =  explode("\n\n", file_get_contents($filename));

$pages = explode("\n", $file_parts[1]);

$rules_right    = array();
$rules_left     = array();

foreach (explode("\n", $file_parts[0]) as $rule) {

    $parts = explode("|", $rule);

    if (array_key_exists($parts[0], $rules_right)) {
        $rules_right[$parts[0]][] = $parts[1];
    } else {
        $rules_right[$parts[0]] = array($parts[1]);
    }

    if (array_key_exists($parts[1], $rules_left)) {
        $rules_left[$parts[1]][] = $parts[0];
    } else {
        $rules_left[$parts[1]] = array($parts[0]);
    }

}

$part_1_sum = 0;
$part_2_sum = 0;

foreach ($pages as $pages_line) {
    $page_list = explode(",", $pages_line);

    $line_ok = true;
    $counter = 0;
    foreach ($page_list as $page) {
        if ($counter < count($page_list) - 1) {
            for ($i = $counter + 1;$i <= count($page_list) - 1;$i++) {
                if (array_key_exists($page, $rules_left)) {
                    if (in_array($page_list[$i], $rules_left[$page])) {
                        $line_ok = false;
                        break 2;
                    }
                }
            }
        }

        if ($counter > 0) {
            for ($i = $counter - 1;$i >= 0;$i--) {
                if (array_key_exists($page, $rules_right)) {
                    if (in_array($page_list[$i], $rules_right[$page])) {
                        $line_ok = false;
                        break 2;
                    }
                }
            }
        }

        $counter++;
    }

    if ($line_ok) {
        $part_1_sum += intval($page_list[intval(count($page_list) / 2)]);

    } else {
        $part_2_sum += intval($page_list[intval(count($page_list) / 2)]);
    }
    
}

echo "Solution for Part 1: {$part_1_sum}\n";
