import requests
import re
from pymemcache.client import Client

# User defined variables
feedaddr = 'http://www.mirc.com/servers.ini'
feedID = 'mircdomains'
mkey = 'fetcher_mircDomain:feeddata'
killchain = 'unknown'

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
	if re.search('^;', x): continue
	if len(x) == 0: continue
	if not re.search('\:', x): continue
	xlist = x.split(':')
	print("%s,%s,%s,%s" % (xlist[1].lower(), feedID, killchain, 'mIRC domain'))
	
