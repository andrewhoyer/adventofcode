<?php

class Splitter {

	public function split_text(string $str, string $delimiter): array {
		return explode($delimiter, $str);
	}

}

?>