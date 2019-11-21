# In Ruby, an array can store different data types.

my_array = []
my_array << 123
my_array << "Something"
my_array << Time.now

=begin
my_array.each do | element |
	puts element
end
=end

array = [1, 5, [7, 9, 11, ["Treasure", "Trash"], "Sigma"]]
#										  ^
#puts array.dig(2, 3, 1)

volley = ["Ashok", "Chavan", "Karthik", "jesus", "Budha"]
soccer = ["Budha", "Karthik", "Ragu", "Ram"]

#puts volley | soccer 
#puts volley & soccer
#puts volley + soccer
#puts volley - soccer

#puts "A" if [] # empty array = true
puts "A" unless [].empty? # returns true but fails bcs of 'unless'

c = [1, nil, 2, nil, 3, nil, nil, nil, 4, nil, 5]
puts "Compacted: #{c.compact}"
puts "c= #{c}"

print "\n:::::::::::::::::::::::::::\n"

# in order to make the compact output permanent add '!':
puts "Compacted: #{c.compact!}"
puts "c= #{c}"
