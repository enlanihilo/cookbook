<?php

require_once __DIR__ . "/src/autoload.php";

if ( $userApp->verifyCookie() )
{
    setcookie("username", "");
    header("Location: /VulnBank/");
}
else
{
    header("Location: /VulnBank/");
    return false;
}
