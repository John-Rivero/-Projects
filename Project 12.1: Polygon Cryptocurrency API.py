import urllib.request, urllib.parse, urllib.error
import json
import ssl

#ssl certification
cert_none = ssl.create_default_context()
cert_none.check_hostname = False
cert_none.verify_mode = ssl.CERT_NONE

#Polygon API
service_url = "https://api.polygon.io/v3/reference/tickers?market=crypto&active=true&sort=ticker&order=asc&limit=100&apiKey=RZcc5XVgetAL61Sj5IQu1t06piGlJHtZ"
html = urllib.request.urlopen (service_url, context=cert_none)
html1 = html.read().decode()

x = json.loads (html1)
#print (json.dumps(x, indent=4))
#print (len(x))

#Selected information for the cryptocurrency
y = (x['results'])
for y1 in y:
    print ("Cryptocurrency Ticker: ", y1['ticker'])
    print ("Name: ", y1['name'])
    print ("Base currency symbol: ", y1["base_currency_symbol"])
    print ("Currency: ", y1['currency_symbol'])
    print ("Actively Traded?", y1['active'])
    print (' ')

print (len(x))
