<?php require_once __DIR__ . "/../autoload.php"; ?>

<html>
  <head>
    <title>WeakBank</title>
    <link rel="stylesheet" href="<?php echo PUBLIC_PATH;?>/style.css">
  </head>
  <body>
  
  <nav>
  
    <ul>
        <li>
            <a class="nav-link" href="<?php echo ROOT_PATH; ?>">Home</a>
        </li>
        
        <?php if ( isset($_COOKIE["username"]) ) { ?>
        <li>
            <a class="nav-link" href="<?php echo PAGES_PATH; ?>/profile.php">Profile</a>
        </li>
        <li>
            <a class="nav-link" href="<?php echo PAGES_PATH; ?>/operations.php">Operations</a>
        </li>
        <li>
            <a class="nav-link" href="<?php echo ROOT_PATH; ?>/logout.php">Logout</a>
        </li>
        <?php } ?>
    </ul>
  
  </nav>
