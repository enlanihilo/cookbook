<?php 

	include 'functions.php';
?>

<!DOCTYPE html>
<html lang="en">
<head>
        <meta charset="UTF-8">
		<title><?php echo $appTitle; ?></title>
</head>
<body>

<?php

if (isset($_POST['username']))
{
	if ($_POST['password'] == $users[$_POST['username']] ) { 
		echo "ok";
		//set user session and redirect to profile.php
		$userAuth = encode_session_cookie($_POST['username']);
		setcookie('sessId', $userAuth);
		header('Location: profile.php');
		die();
	}	
	else
	{
		header('HTTP/1.0 403 Forbidden');
		die('<h3>Wrong Credentials.</h3>');
	}
}
else { 
	header('HTTP/1.0 403 Forbidden');
	die('<h3>Access Denied.</h3>');
}

?>
</body>
</html>
