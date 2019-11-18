File.open("users.txt", "w") { |f| f.write "#{Time.now} - User logged in.\n"}

