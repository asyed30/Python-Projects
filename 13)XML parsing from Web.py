import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl


# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro



# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url=input('Enter your link-')
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()

print('Retrieved', len(data), 'characters')
#print(data)
tree = ET.fromstring(data)


results = tree.findall('comments/comment/count')
#results=tree.findall('.//comment')
print(results)
z=0
for count in results:
  y=int(count.text)
  z= z+y
  
print(z)




 


