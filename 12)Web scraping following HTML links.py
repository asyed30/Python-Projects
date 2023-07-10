# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
import bs4
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter-')
html = urllib.request.urlopen(url, context=ctx).read()
soup = bs4.BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
humbu=list()
for tag in tags:
 link= tag.get('href',None)
 humbu.append(link)
 

print('First link',humbu[17])



url2 = humbu[17]
html2 = urllib.request.urlopen(url2, context=ctx).read()
soup2 = bs4.BeautifulSoup(html2, 'html.parser')

# Retrieve all of the anchor tags
tags2 = soup2('a')
humbu2=list()
for tag2 in tags2:
 link= tag2.get('href',None)
 humbu2.append(link)
 
print('Second link',humbu2[17])



url3 = humbu2[17]
html3 = urllib.request.urlopen(url3, context=ctx).read()
soup3 = bs4.BeautifulSoup(html3, 'html.parser')

# Retrieve all of the anchor tags
tags3 = soup3('a')
humbu3=list()
for tag3 in tags3:
 link= tag3.get('href',None)
 humbu3.append(link)
 
print('Third link',humbu3[17])

url4 = humbu3[17]
html4= urllib.request.urlopen(url4, context=ctx).read()
soup4 = bs4.BeautifulSoup(html4, 'html.parser')

# Retrieve all of the anchor tags
tags4 = soup4('a')
humbu4=list()
for tag4 in tags4:
 link= tag4.get('href',None)
 humbu4.append(link)
 
#print('Length of humbu4:', len(humbu4))


# Check if the index is valid
if len(humbu4) > 17:
    print('Fourth link', humbu4[17])
else:
    print('Invalid index for humbu4')
 
# print('Fourth link',humbu4[17])
 
 
url5 = humbu4[17]
html5= urllib.request.urlopen(url5, context=ctx).read()
soup5 = bs4.BeautifulSoup(html5, 'html.parser')

# Retrieve all of the anchor tags
tags5= soup5('a')
humbu5=list()
for tag5 in tags5:
 link= tag5.get('href',None)
 humbu5.append(link)
 
print('Fifth link',humbu5[17])


url6 = humbu5[17]
html6= urllib.request.urlopen(url6, context=ctx).read()
soup6 = bs4.BeautifulSoup(html6, 'html.parser')

# Retrieve all of the anchor tags
tags6= soup6('a')
humbu6=list()
for tag6 in tags6:
 link= tag6.get('href',None)
 humbu6.append(link)
 
print('Sixth link',humbu6[17])

url7 = humbu6[17]
html7= urllib.request.urlopen(url7, context=ctx).read()
soup7 = bs4.BeautifulSoup(html7, 'html.parser')

# Retrieve all of the anchor tags
tags7= soup7('a')
humbu7=list()
for tag7 in tags7:
 link= tag7.get('href',None)
 humbu7.append(link)
 
print('Seventh link',humbu7[17])



 
 






 
 
 
 








