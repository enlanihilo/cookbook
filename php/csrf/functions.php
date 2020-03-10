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
		global $specialToken;
		global $users;

		//base64 decode cookie
		$sessid = base64_decode($_COOKIE['sessId']);
		
		// strip specialToken away from cookie
		$userFromCookie = str_replace($specialToken, '', $sessid);

		//verify if $specialToken is present
		if ( $userFromCookie )
		{
			echo 'user: ';
			echo $userFromCookie;

			if (isset($users[$userFromCookie]))
			{
				echo "<br>username will be changed!";
			}
		}
		else
		{
			die('Forbidden');
			return false;
		}

		return true;
	}

?>
