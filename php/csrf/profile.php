<!DOCTYPE html>
<html lang="en">
<head>
        <meta charset="UTF-8">
        <title></title>
</head>
<body>

<?php

	if (!isset($_COOKIE['sessId']))
	{
		header('Location: index', true, 301);
		die();
	}
?>

        <div class="container">
			<!--profile actions-->
			<form id="changeUser" action="/actions.php" method="GET">
				<input type="text" name="newuser">
				<input type="hidden" name="csrfToken" value="<?php echo $_COOKIE['sessId']; ?>>">
				<input type="submit" value="change username">
			</form>
			<form id="changePwd" action="/actions.php" method="GET">
				<input type="text" name="newuser">
				<input type="submit" value="change username">
			</form>
			<form id="deleteAcc" action="/actions.php" method="GET">
				<input type="text" name="newuser">
				<input type="submit" value="change username">
			</form>
		</div>

		<button id="logout">Logout</button>

<script>
		
		let changeUser = document.querySelector('#changeUser');
		let changePwd = document.querySelector('#changePwd');
		let deleteAcc = document.querySelector('#deleteAcc');
		let logout = document.querySelector('#logout');

		logout.onclick = () => {
			//delete cookie and return to the index page
		}

	</script>

</body>
</html>
