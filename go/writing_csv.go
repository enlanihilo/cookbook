package main

import (
	"os"
	"fmt"
)


func main() {

	employees :=[]string{"Mary, 35, Software Developer","John, 22, Network Engineer","Peter, 18, Web Developer","Lana, 19, Web Developer"}

	csvFile, err := os.Create("test.csv")
	if err != nil {
		fmt.Println(err)
	}

	csvFile.WriteString("name, age, profession\n")

	for i:=0; i<len(employees); i++ {
		csvFile.WriteString(employees[i])
		csvFile.WriteString("\n")
	}

	fmt.Println("csv file with employees created.")

}
