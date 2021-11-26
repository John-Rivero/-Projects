import urllib.request, urllib.parse, urllib.error
import json
import ssl

#ssl certification
cert_none = ssl.create_default_context()
cert_none.check_hostname = False
cert_none.verify_mode = ssl.CERT_NONE

service_url = "https://api.polygon.io/v3/reference/tickers?market=crypto&active=true&sort=ticker&order=asc&limit=10&apiKey=RZcc5XVgetAL61Sj5IQu1t06piGlJHtZ"
html = urllib.request.urlopen (service_url, context=cert_none)
html1 = html.read().decode()

x = json.loads (html1)

#print ('User count: ', len(x))
print(json.dumps(x, indent=4))

#not finished
