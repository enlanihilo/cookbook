#1 generate pseudo random n between x,y
#2 ask for user guess
#3 check if they r equal

$chances = 3
$random_number = ( rand() * 100 ).to_i


while $chances > 0 do
	
	print "\nYou have #{$chances} chances\nChoose a number between 0 - 100 >> "
	$user_guess = gets.to_i

	if $random_number == $user_guess
		puts "You won!"
		exit!
	elsif $random_number < $user_guess
		puts "My number is smaller!"
		$chances -= 1
	else
		puts "My number is bigger!"
		$chances -= 1
	end
end

puts "You Lost!!!\nMy number was #{$random_number}"
