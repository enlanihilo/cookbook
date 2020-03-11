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
		global $users;
		global $specialToken;

		//base64 decode cookie
		$sessid = base64_decode($_COOKIE['sessId']);
		
		// strip specialToken away from cookie
		$userFromCookie = str_replace($specialToken, '', $sessid);

		//verify if $specialToken is present
		if ( $userFromCookie )
		{
			echo 'user: <p style="color: red">'
					. $userFromCookie
					. '</p>';

			if (isset($users[$userFromCookie]))
			{
					echo " will be changed to " 
							. "<p style='color: blue'>" 
							. $_POST['newuser']
							. "</p>";
			}
			else
			{
				header('HTTP/1.0 500 Internal Server Error');
				die('username not present in db');
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
