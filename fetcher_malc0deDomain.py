import requests
import re
from pymemcache.client import Client

# User defined variables
feedaddr = 'http://malc0de.com/bl/BOOT'
feedID = 'malc0de'
mkey = 'fetcher_malc0deDomain:feeddata'
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

print('domain,feedID,killchain,description')

for x in splitlines:
	x = x.strip()
	if re.search('^\/\/', x): continue
	if len(x) == 0: continue
	xsplit = x.split()
	print("%s,%s,%s,%s" % (xsplit[1], feedID, killchain, 'Malicious domain'))
	
