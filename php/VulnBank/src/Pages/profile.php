<?php

require_once __DIR__ . "/../autoload.php";
require_once __DIR__ . "/../Templates/htmlTop.php";

if ( $userApp->verifyCookie() )
{
    $title = $userApp->sessionCookie . "'s profile";
    $userBalance = $userApp->getBalance();
    
    echo "<section class='p-1'>"
         . "  <h2>" . $title . "</h2>"
         . "  <p>Money Available: $" . $userBalance . "</p>"
        . "</section>";
}

require_once __DIR__ . "/../Templates/htmlBottom.php";
