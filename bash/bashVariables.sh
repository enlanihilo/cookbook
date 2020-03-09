#!/bin/bash

: '
	
	Bash does not segregate its variables by "type". 

	Essentially, Bash variables are character strings, but depending on context, Bash permits
	arithmetic operations and comparisons on variables. The determining factor is whether the
	value of a variable contains only digits.

	Utyped variables are both a blessing and a curse, they permit more flexibility in scripting
	and make it easier to grind out lines of code (and give you enough rope to hang yourself!)
	However, they likewise permit subtle errors to creep in and encourage sloppy programming
	habits.

	Bash does permit declaring variables: tldp.org/LDP/abs/html/declareref.html
'

num1=100 	# integer
let "num1 += 1"
# echo "num1 = $num1" 	# integer, still

num2=BB35
# echo $num2

num3="Ajsaifu90f"
# echo $num3

######################## DECLARING VARIABLES ######################## 

: '

	declare --type <variable_name>

	-r readonly 
	-i integer
	-f functions
	-a array
	-x export

'

declare -i var1=1
echo $var1

