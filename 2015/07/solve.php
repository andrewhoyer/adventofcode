<?php

$filename   = $argv[1];
$handle     = fopen($filename, 'r');
$lines      = explode("\n", fread($handle, filesize($filename)));

fclose($handle);

$gates = array();

// Create all of the gates first

foreach ($lines as $line) {
    $parts = explode(' -> ', $line, strlen($line));
    $gates[$parts[1]] = array( 'value' => -1, 'instructions' => $parts[0], 'gate' => $parts[1], 'set' => false);
}

// Loop repeatedly through each line, assigning values to gates. In cases where
// other gates are used, those are only calculated when the gates in the instructions
// have a value as well.

$complete = false;

while ($complete == false) {
    
    $complete = true;

    foreach ($lines as $line) {
        
        $parts = explode(' -> ', $line, strlen($line));

        if ($gates[$parts[1]]['set'] == true) {
            // Gate is already set
            continue;

        } else {
            
            if (is_numeric($parts[0])) {
                // It's a straight assignment.

                $gates[$parts[1]]['value']  = (int)$parts[0];
                $gates[$parts[1]]['set']    = true;

            } else if (str_contains($parts[0], 'AND')) {
                // There are more checks here because the possibilities are more varied.
                // Examples:
                // aa AND bb
                // 1 AND aa

                $instructions = explode(' ', $parts[0], strlen($parts[0]));

                // In the puzzle data, only the left item in the list can be a gate or a 1.
                $left = '';

                if (is_numeric($instructions[0])) {
                    // If it's a number, set the integer value
                    $left = (int)$instructions[0];

                } else if (!$gates[$instructions[0]]['set']) {
                    // Otherwise it's a gate. If not set, continue.
                    $complete = false;
                    continue;

                } else {
                    // It's a gate, and the gate it set, so get the value
                    $left = $gates[$instructions[0]]['value'];

                }

                // Next, check to see if the right gate is set. If not, continue.
                if (!$gates[$instructions[2]]['set']) {
                    $complete = false;
                    continue;
                }

                // If all checks above ar eokay, do the AND calculation.
                $gates[$parts[1]]['value']  = ($left & $gates[$instructions[2]]['value']) & 0xFFFF;
                $gates[$parts[1]]['set']    = true;

            } else if (str_contains($parts[0], 'OR')) {
                // OR lines are simpler, containing two gates.

                $instructions = explode(' ', $parts[0], strlen($parts[0]));

                if (!$gates[$instructions[0]]['set'] || !$gates[$instructions[2]]['set']) {
                    $complete = false;
                    continue;
                }

                $gates[$parts[1]]['value']  = ($gates[$instructions[0]]['value'] | $gates[$instructions[2]]['value']) & 0xFFFF;
                $gates[$parts[1]]['set']    = true;

            } else if (str_contains($parts[0], 'LSHIFT')) {
                $instructions = explode(' ', $parts[0], strlen($parts[0]));

                if (!$gates[$instructions[0]]['set']) {
                    $complete = false;
                    continue;
                }
                
                $gates[$parts[1]]['value']  = ($gates[$instructions[0]]['value'] << (int)$instructions[2]) & 0xFFFF;
                $gates[$parts[1]]['set']    = true;

            } else if (str_contains($parts[0], 'RSHIFT')) {
                $instructions = explode(' ', $parts[0], strlen($parts[0]));

                if (!$gates[$instructions[0]]['set']) {
                    $complete = false;
                    continue;
                }

                $gates[$parts[1]]['value']  = ($gates[$instructions[0]]['value'] >> (int)$instructions[2]) & 0xFFFF;
                $gates[$parts[1]]['set']    = true;

            } else if (str_contains($parts[0], 'NOT')) {                
                $instructions = explode(' ', $parts[0], strlen($parts[0]));

                if (!$gates[$instructions[1]]['set']) {
                    $complete = false;
                    continue;
                }

                // This is the only line that really needs the conversion to a 
                // 16-bit integer with & 0xFFFF, although it was added to all of them.
                // Also note that order of operations here require brackets as placed.
                $gates[$parts[1]]['value']  = (~$gates[$instructions[1]]['value']) & 0xFFFF;
                $gates[$parts[1]]['set']    = true;

            }  else { 
                // A straight assignment, but with another gate.

                if (!$gates[$parts[0]]['set']) {
                    $complete = false;
                    continue;
                }

                $gates[$parts[1]]['value']  = $gates[$parts[0]]['value'];
                $gates[$parts[1]]['set']    = true;
                
            }

        }
        
    }

}

echo("The value of gate 'a' is: " . $gates['a']['value'] . "\n");
