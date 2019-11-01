package main

import (
	"fmt"
	"database/sql"
	_ "github.com/go-sql-driver/mysql"
)


func main() {

	//create database handle	user:@/passw
	db, _ := sql.Open("mysql", "tester:@/")
	defer db.Close()

	//connection and check server version
	var version string
	db.QueryRow("SELECT VERSION()").Scan(&version)
	fmt.Println("Connected to:", version)

}
