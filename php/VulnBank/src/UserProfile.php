<?php

class UserProfile extends App
{
    public $sessionCookie;

    public function __construct()
    {
        if (isset($_COOKIE["username"])) {
        
            $this->sessionCookie = $_COOKIE["username"];
        }
        else
        {
            // nothing
        }
        
    }

    public function verifyCookie(): bool
    {
        $userIsValid = $this->verifyLogin($this->sessionCookie);
        
        if ( $userIsValid )
        {
            return true;
        }
        else
        {
            return false;
        }
    }
    
    public function getBalance(): float
    {
        return $this->getUser($this->sessionCookie)["balance"];
    }
}
