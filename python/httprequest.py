import urllib.request as urr
import urllib.parse as urp

url = "http://httpbin.org/"

#GET request
getreq = urr.urlopen(url)
#print(getreq.read())

#POST request
url_post = url+"post"

post_data = urp.urlencode({
    "name" : "Mr. Nobody",
    "location" : "wild",
    "language" : "python"
}).encode("ascii")

post_response = urr.urlopen(url=url_post, data=post_data)
#print(post_response.read())


