#https://rickandmortyapi.com/api/character
#To choose character add a (/) + (#) at the end. For example (/2)

import urllib.request, urllib.parse, urllib.error
import json
import ssl

#ssl certification
cert_none = ssl.create_default_context()
cert_none.check_hostname = False
cert_none.verify_mode = ssl.CERT_NONE

#change character by changing the number at the end of the url
service_url = "https://rickandmortyapi.com/api/character/2"
html = urllib.request.urlopen (service_url, context=cert_none)
html1 = html.read().decode()

x = json.loads (html1)

#print ('User count: ', len(x))
#print(json.dumps(x, indent=4))

print ('Character Name: ', x['name'])
print ('Species: ', x['species'])
print ('Origin: ', x["origin"]['name'])
