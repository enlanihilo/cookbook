<!DOCTYPE html>
<html lang="en">
<head>
        <meta charset="UTF-8">
        <title></title>
</head>
<body>
	<h1>Fetch A Server's Response Headers</h1>
	<form action="/" method="GET">
		<input type="text" name="website">
		<input type="submit" value="GET HEADERS">
	</form>

	<?php
		if ( isset($_GET['website']) )
		{
			$www = 'https://' . $_GET['website']; #must sanitize
			$headers = get_headers($www, 1);
			print_r($headers);
		}
	?>

</body>
</html>

