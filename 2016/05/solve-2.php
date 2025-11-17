<?php

$visualize = false;

$door = "ffykfhsq";
$password = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '];

$counter = 0;
while (in_array(' ', $password)) {

    while (true) {

        $md5 = md5($door . $counter);

        if (substr($md5, 0, 5) === '00000') {
            // First 5 digit check

            if (is_numeric(substr($md5, 5, 1))) {    
                // 6th character must be numeric

                if (intval(substr($md5, 5, 1)) < 8) {
                    // 6th must be less than 8
                
                    if ($password[intval(substr($md5, 5, 1))] === ' ') {
                        // Position in password must not already be used

                        $password[intval(substr($md5, 5, 1))] = substr($md5, 6, 1);
                        
                        if ($visualize) visualize();
                        
                        $counter++;
                        break;

                    }
                }
            }
        }

        if ($visualize) visualize();
        //if ($visualize) usleep(90); // Optional pause in microseconds

        $counter++;

    }

}

print("Part 2 solution: " . implode('', $password) . "\n");
exit();


function visualize() {
    global $md5;
    global $password;
    global $counter;
    global $door;

    system('clear'); // Comment out for major speed increase
    print($door . $counter . "\t");
    print($md5 . "\t");
    print(implode('', $password) . "\n");

}
