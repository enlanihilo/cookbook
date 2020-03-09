#!/bin/bash

: '

	-eq equal 			-ne not equal
	-lt less than 		-le less than or equal to
	-gt greater than 	-ge greater than or equal to

'

age=15

if [ $age -ge 18 ] && [ $age -le 90 ]
then
		echo "you can drive"
elif [ $age -ge 15  ] 
then
		echo "you can own a mini-scooter"
else
		echo "you can't drive"
fi



