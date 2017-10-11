import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url- ')
count = int(input('Enter count- '))
position = int(input('Enter position- '))

for i in range(count):
	html = urllib.request.urlopen(url, context=ctx).read()
	soup = BeautifulSoup(html, 'html.parser')

	# Retrieve all of the anchor tags
	tags = soup('a')
	links = []
	for tag in tags:
	   	x = tag.get('href', None)
	   	links.append(x)
	url = links[position-1]
	print(url)
print("Final:", url)