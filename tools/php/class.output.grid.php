<?php

class OutputGrid {

	public function output_grid(array $grid): void {
		
		$min_x = 0;
		$max_x = 0;
		$min_y = 0;
		$max_y = 0;

		foreach (array_keys($grid) as $test) {
			//print($test."\n");
			$coords = explode(',', $test);
			//print(var_dump($coords));
			if (intval($coords[0]) < $min_x) {
				$min_x = intval($coords[0]);
			}

			if (intval($coords[0]) > $max_x) {
				$max_x = intval($coords[0]);
			}

			if (intval($coords[1]) < $min_y) {
				$min_y = intval($coords[1]);
			}

			if (intval($coords[1]) > $max_y) {
				$max_y = intval($coords[1]);
			}
		}

		for ($y = $min_y;$y <= $max_y;$y++) {
			for ($x = $min_x;$x <= $max_x;$x++) {
				if (array_key_exists($x . ',' . $y, $grid)) {
					print($grid[$x . ',' . $y]);
				} else {
					print("⬛️");
				}
			}
			print("\n");

		}

		return;

	}

}

?>