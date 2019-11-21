def from1_to5
	(1..5).each do |num|
		puts num
	end
end

def fromBAD_toBAG
	("bad".."bag").each do | char | 
		puts "#{char} "
	end
end

def range_classes
	a = -4..10
	puts "'a' class = #{a.class}\n" \
		 "maximum value in range = #{a.max}\n" \
		 "minimum value in range = #{a.min}"
end

def range_case
	puts "Student grading system"
	print "Enter student mark: "

	mark = gets.chop.to_i
	grade = case mark
		when 80..100
			"A"
		when 60..79
			"B"
		when 40..59
			"C"
		when 0..39
			"D"
		else
			"Unable to determine grade. try again."
		end

	puts "Your grade is #{grade}"
end

def check_intervals
	print "Enter any letter: "
	letter = gets.chop

	puts "You have entered a lower case letter" if ('a'..'z') === letter
	puts "You have entered an upper case letter" if ('A'..'Z') === letter
end

def three_dots
	three_dots = (1...5).to_a
	two_dots = (1..5).to_a

	puts "(1...5) =>  #{three_dots}\n" \
		 "(1..5) =>  #{two_dots}"
end

def endless_ranges
	print "Enter your age: "
	age = gets.chop.to_i

	case age
	when (21..)
		puts "You are an adult"
	else
		puts "You are young"
	end
end



