<?php

class Splitter {

	public function split_text(string $str, string $delimiter): array {
		return explode($delimiter, $str);
	}

	public function str_to_array(string $str): array {
		$chars = [];

		for ($i = 0;$i < strlen($str);$i++) {
			$chars[] = substr($str, $i, 1);
		}

		return $chars;
	}

}

?>