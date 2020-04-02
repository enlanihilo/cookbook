<?php

require_once __DIR__ . "/../autoload.php";

require_once __DIR__ . "/../Templates/htmlTop.php";

if ( $userApp->verifyCookie() )
{
    $title = $userApp->sessionCookie . "'s Operations:";
    
    echo "<h1>" . $title . "</h1>";
    require_once __DIR__ . "/../Templates/operations/deposit.php";
    
}

require_once __DIR__ . "/../Templates/htmlBottom.php";
