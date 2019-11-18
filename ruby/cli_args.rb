=begin

Ruby captures command line arguments with a special
array named ARGV (just like C!).

When written inside your Ruby program, ARGV will take
a command line args like:

	ruby cli_args.rb these are elements

	ARGV = ["these", "are", "elements"]

> in C argv[0] returns the name of the program, how to do that in ruby?

$0
__FILE__
$PROGRAM_NAME

=end

if ARGV.length < 1
	abort("Usage: ruby #{$0} arg1 arg2 arg-N")
else
	ARGV.each do |argument|
		puts "Processing #{argument}..."
	end
end

