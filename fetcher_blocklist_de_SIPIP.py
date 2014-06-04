import requests
import re
from pymemcache.client import Client

# User defined variables
feedaddr = 'http://www.blocklist.de/lists/sip.txt'
feedID = 'blocklist_de_sip'
mkey = 'fetcher_blocklist_de_SIPIP:feeddata'
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

print('ipv4,feedID,killchain,description')

for x in splitlines:
	x = x.strip()
	if re.search('^#', x): continue
	if re.search('\:', x): continue # Skip IPv6
	if len(x) == 0: continue
	print("%s,%s,%s,%s" % (x, feedID, killchain, 'SIP scanners'))
	
