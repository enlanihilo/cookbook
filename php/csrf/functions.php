<?php
	
	include 'data.php';

	$specialToken = 'a97xv98x09';

	function encode_session_cookie($username)
	{
		global $specialToken;
		$encoded_session = "";

		//concatenate $username with $specialToken
		$encoded_session .= $username . $specialToken;

		//base64 encode it
		return base64_encode($encoded_session);
	}

	function decode_session_cookie()
	{
		$sessionId = $_COOKIE['sessId'];

		//base64 decode
		base64_decode($sessionId);
	
		//verify if $specialToken is present
		if (preg_match('/' . $specialToken  . '/', $sessId))
		{
			// extract username from cookie
			$userFromCookie = str_replace($specialToken, "", $sessId);
		}

		//check if username exists in users "db"
		if (isset($users[$userFromCookie]))
		{
			echo "username will be changed!";
		}

		return true;
	}

?>
