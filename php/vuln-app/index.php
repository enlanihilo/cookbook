<?php

	header('X-Powered-By: ');
	# header('Location: https://bing.com');
?>

<!DOCTYPE html>
<html lang="en">
<head>
        <meta charset="UTF-8">
        <title>don't hack me</title>
</head>
<link rel="stylesheet" href="./main.css">
<body>

	<nav>
		<ul class="pd1">
		    <li><a href="/">Home</a></li>
		    <li><a href="/register.php">Register</a></li>
			<li><a href="/about.html">About us</a></li>
		</ul>
	</nav>

	<main class="pd2">
		<h1>dummy web app</h1>

		<div class="container pd1">
			<form action="/" method="GET">
				<input type="text" name="q">
				<input type="submit" value="send">
			</form>
		</div>
	
		<div class="container pd1">
			<?php
				if ( isset( $_GET['q'] ) )
				{
					$userinput = strip_tags( $_GET['q'] );;
					echo '<h2>Sanitized:</h2>';
					echo 'Searching for ' .  $userinput;
				}
			?>
		</div>
		<!--
		<div class="container pd1">
			<form action="/" method="POST">
				<input type="text" name="s">
				<input type="submit" value="send">
			</form>
		</div>-->

		<div class="container pd1">
			<?php
				if ( isset( $_GET['q'] ) )
				{
					echo '<h2>Not Sanitized:</h2>';
					echo 'Searching for ' . $_GET['q'];
				}
			?>
		</div>

	</main>

</body>
</html>
