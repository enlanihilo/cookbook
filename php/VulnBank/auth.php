<?php require_once __DIR__ . "/src/autoload.php"; 


if ( $_SERVER["REQUEST_METHOD"] === "POST" )
{
    if ( isset($_POST["login"]) && isset($_POST["password"]) ) 
    {
        $login = $_POST["login"];
        $password = $_POST["password"];
        
        $userIsAuthenticated = $app->authenticate($login, $password);
        
        if ( $userIsAuthenticated )
        {
            // load profile page
            setcookie("username", $login);
            header("Location: /VulnBank/src/Pages/profile.php");
        }
    }
    else
    {
        $app->raiseError();
        echo "<a href='../VulnBank/' class='error'>go back</a>";
    }
    
}
