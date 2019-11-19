require 'httparty'

puts "domain > "
domain = gets.chomp

r = HTTParty.get("https://#{domain}")
statusCode = r.response.code

system "clear"
puts "#{domain} returned status code : #{statusCode}"


