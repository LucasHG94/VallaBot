import urllib2
import json

req = urllib2.Request("https://api.forecast.io/forecast/bc81c2ffb5df746f4ad745932d67c536/41.651981,%20-4.728561")
opener = urllib2.build_opener()
f = opener.open(req)
json = json.loads(f.read())
print json["currently"]
