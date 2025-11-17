<?php

$visualize = false;

$door = "ffykfhsq";
$password = "";

$counter = 0;
while (strlen($password) < 8) {

    while (true) {

        $md5 = md5($door . $counter);

        if (substr($md5, 0, 5) === '00000') {
            $password .= substr($md5, 5, 1);
            
            if ($visualize) visualize();

            $counter++;
            break;
        }

        if ($visualize) visualize();
        //if ($visualize) usleep(90); // Optional delay in microseconds

        $counter++;

    }

}

print("Part 1 solution: " .$password . "\n");
exit();


function visualize() {
    global $md5;
    global $password;
    global $counter;
    global $door;

    system('clear'); // Comment out for major speed improvement
    print($door . $counter . "\t");
    print($md5 . "\t");
    print($password . "\n");

}
