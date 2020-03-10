
<?php

	//init server with: php -S localhost:7777

	// any origin can fetch data from this server
	$origin = [
		'any' => '*',
		'google' => 'https://bing.com',
		'stackoverflow' => 'https://stackoverflow.com'
	];

	header('Access-Control-Allow-Origin: ' . $origin['stackoverflow']);
	header('Accept: */*');
	header('X-Powered-By: Express');

	echo 'served successfully';

?>


