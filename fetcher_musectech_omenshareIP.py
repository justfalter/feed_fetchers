import requests
import re
from pymemcache.client import Client

feedaddr = 'http://www.musectech.com/omens/omenshare.txt'
feedID = 'musectech'
mkey = 'fetcher_musectech_omenshareIP:feeddata'
killchain = 'Reconnaissance'

client = Client(('localhost', 11211))
result = client.get(mkey)

if isinstance(result, str):
	splitlines = result.split('\n')
else:
	r = requests.get(feedaddr)
	client.set(mkey, r.content, expire=7200)
	splitlines = r.content.split('\n')

print('ipv4,feedID,killchain,description,context')

for x in splitlines:
	x = x.strip()
	if re.search('^\*', x): continue
	if len(x) == 0: continue
	xsplit = x.split(':')
	if re.search('[a-z,A-Z]', xsplit[1]): continue
	if not re.search('\.', xsplit[1]): continue
	if re.search('\/', xsplit[1]): continue
	if re.search('\.$', xsplit[1]):
		xsplit[1] = xsplit[1] + '0/24'
	print("%s,%s,%s,%s,%s" % (xsplit[1], feedID, killchain, 'Musectech hostile IPs',xsplit[2]))
	
