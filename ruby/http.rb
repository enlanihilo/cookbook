require 'net/http'

uri = URI("https://www.bing.com")
res = Net::HTTP.get_response(uri)

puts res.body if res.is_a?(Net::HTTPSuccess)
