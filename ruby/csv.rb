File.open("test.csv", "w") { |f| 
	f.write "Username, Password\n"
	f.write "JohnDoe, Password123\n"
	f.write "AllieB, Password321\n"
	f.write "JohnTT, Password456\n"
}

