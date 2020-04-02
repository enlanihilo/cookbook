<?php require_once __DIR__ . "/src/Templates/htmlTop.php"; ?>
    
    <main>

        <h1>Vulnerable Bank</h1>

        <form method="POST" action="/VulnBank/auth.php">
            <div class="input-container">
                <label>Login: </label>
                <input type="text" name="login" required/>
            </div>
            
            <div class="input-container">
                <label>Password: </label>
                <input type="password" name="password" required/>
            </div>
            
            <div class="input-container">
                <input class="btn" type="submit" value="log" />
            </div>
        </form>

    </main>
    
<?php require_once __DIR__ . "/src/Templates/htmlBottom.php"; ?>
