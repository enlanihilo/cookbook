<!DOCTYPE html>
<html lang="en">
<head>
        <meta charset="UTF-8">
        <title></title>
</head>
<body>

<?php

	include 'functions.php';

	if (! isset($_COOKIE['sessId']))
	{
		header('HTTP/1.0 403 Forbidden');
		die('Access denied');
	} 
	else if (isset($_POST['session']) && $_POST['session'] == 'kill')
	{

		setcookie('sessId', '');
		header('HTTP/1.0 301');	
		header('Location: /index.php');
	}
	else
	{
		// verify if user and sessId match
		decode_session_cookie();
	}

?>

</body>
</html>
