<?php

class App
{
    private $users = [
        "alice" => [
            "password" => "pass123",
            "balance" => 500
        ],
        "bob" => [
            "password" => "hunter2",
            "balance" => 250
        ]
    ];
    
    public $errorMsg = [
        0 => "Invalid login.",
        1 => "Invalid password.",
        2 => "Unauthorized."
    ];
    
    public function __construct( $debug = false )
    {
        if ( $debug ) 
        {
            // print all users
            echo "<pre>", var_dump($this->users), "</pre>";
        }
    }
    
    public function raiseError( $errorCode = 2 )
    {
        echo "<div class='error-container'>"
            . "<p>"
            . $this->errorMsg[$errorCode]
            . "</p>"
            ."</div>";
    }
    
    public function getUser($name)
    {
        return $this->users[$name];
    }
    
    public function authenticate($login, $password): bool
    {
    /*
    *   Set user session
    */
        if ( $this->verifyLogin($login) )
        {
                if ( $this->verifyPassword($login, $password) )
                {
                    return true;
                }
                else
                {
                    return false;
                }
        }
        else
        {
            return false;
        }
    }
    
    public function verifyLogin($login): bool
    {
        if ( isset($this->users[$login]) )
        {
            return true;
        }
        else
        {
            $this->raiseError(0);
            return false;
        }
    }
    
    private function verifyPassword($login, $password): bool
    {
        if ( $this->users[$login]["password"] === $password )
        {
            return true;
        }
        else
        {
            $this->raiseError(1);
            return false;
        }
    }
}
