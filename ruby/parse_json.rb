require 'json'

file = File.open "./dummy.json"
data = JSON.load file # returns a hash
#puts data.is_a? Hash
file.close

#puts data.keys
puts data["title"]
