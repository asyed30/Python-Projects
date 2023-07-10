import urllib.request, urllib.parse, urllib.error
import  json
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
info = json.loads(data)
cnt=0
z=info['comments']
print (z)
for item in z:
	x=item['count']
	y=int(x)
	cnt=cnt+y
	
print(cnt)
	
	
