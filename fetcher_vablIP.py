import requests
import re
import socket
from pymemcache.client import Client

# User defined variables
feedaddr = 'http://www.infiltrated.net/vabl.txt'
feedID = 'vabl'
mkey = 'fetcher_vablIP:feeddata'
killchain = 'Reconnaissance'

# No user modifications needed below.
client = Client(('localhost', 11211))
result = client.get(mkey)

if isinstance(result, str):
	splitlines = result.split('\n')
else:
	r = requests.get(feedaddr)
	client.set(mkey, r.content, expire=7200)
	splitlines = r.content.split('\n')

seen = []

print('ipv4,feedID,killchain,description')

for x in splitlines:
	x = x.strip()
	if not re.search('^\d', x): continue
	x = re.sub(' .*$', '', x)
	if len(x) == 0: continue
	if x in seen: continue
	seen.append(x)
	try:
		socket.inet_aton(x)
	except socket.error:
		continue
	print("%s,%s,%s,%s" % (x, feedID, killchain, 'Malicious host'))
	
