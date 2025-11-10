<?php

$visualize = false;

$filename   = $argv[1];
$handle     = fopen($filename, 'r');
$lines      = explode("\n", fread($handle, filesize($filename)));

fclose($handle);

// Part 1. Determine valid rooms only

$valid_rooms = [];
$sum = 0;

foreach ($lines as $line) {

    $parts  = preg_split("/\d+/", $line);

    $door   = str_replace("-", "", $parts[0]);
    $name   = preg_replace("/[\[\]]/", "", $parts[1]);
    $sector = intval(preg_replace("/[^\d]/", "", $line));

    $chars  = [];

    foreach (str_split($door) as $char) {

        if ($visualize) system('clear');

        if (array_key_exists($char, $chars)) {
            $chars[$char]++;
        } else {
            $chars[$char] = 1;
        }

        // Sort the array, first by the value, and if those are
        // equal, by the key alphabetically.
        // It would be more efficient to put it outside the
        // foreach block, but it makes the visualization better.
        uksort($chars, function($key1, $key2) use ($chars) {
            $val1 = $chars[$key1];
            $val2 = $chars[$key2];

            if ($val1 != $val2) {
                return $val2 <=> $val1; // descending by value
            }

            return strcasecmp($key1, $key2); // ascending by key (case-insensitive)
        });

        if ($visualize) {
            foreach ($chars as $key => $val) {
                print $key;
            }
            print("\n");

            foreach ($chars as $key => $val) {
                print $val;
            }
            print("\n");        
        }

        if ($visualize) usleep(50000); // microseconds
    }

    $chars = array_slice($chars, 0, 5);

    $text = implode("", array_keys($chars));
    
    if ($visualize) print("Check: $text\nData:  $name\n");
    
    if ($text == $name) {
        if ($visualize) print("VALID ROOM\n");

        $valid_rooms[] = [$parts[0], $sector, $name];
        $sum += $sector;
    } else {
        if ($visualize) print("NOT A VALID ROOM\n");
    }

    if ($visualize) usleep(2000000); // microseconds

}

print("Part 1 solution: " .$sum . "\n");


// Part 1. Use a ceaser chipher, shifting each letter the number of the
// sector. Results are rooms like "international egg shipping", and
// the one being searched for is "where North Pole objects are stored"
// The script does not produce a distinct answer. Instead, it prints
// a list of room names that can be searched for "north" to locate the
// correct room, and its corresponding sector (the actual answer)

$alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'];

foreach ($valid_rooms as $room) {
    
    print("Sector $room[1]\t");
    
    foreach (str_split($room[0]) as $char) {

        // Dashes are simply converted to spaces
        if ($char == '-') {
            print(" ");
        } else {

            // A simple caesar cipher implementation
            $start = array_search($char, $alphabet);

            // Forget looping! Just get the mod.
            $start += $room[1] % count($alphabet);
            
            // Then if it's beyond the range of the array, subtract the
            // count to find the correct location.
            if ($start > count($alphabet) - 1) {
                $start -= count($alphabet);
            }

            print($alphabet[$start]);
        }
    }

    print("\n");

}

exit();
