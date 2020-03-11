<?php

	header('Access-Control-Allow-Origin: https://stackoverflow.com');
	header('X-Powered-By: ');

?>

<!DOCTYPE html>
<html lang="en">
<head>
        <meta charset="UTF-8">
        <title></title>
</head>
<body>
<form action="/auth.php" method="POST">
	<input type="text" name="username">
	<input type="password" name="password">
	<input type="submit" value="login">
</form>

</body>
</html>
