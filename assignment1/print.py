import urllib
import json

response = urllib.urlopen("http://search.twitter.com/search.json?q=microsoft")
pyresponse = json.load(response)

#print pyresponse["results"]
#print type(pyresponse["results"])

results = pyresponse['results']
#print results[0].keys()
#print results[0]['text']

for i in range(10):
    print results[i]['text']
