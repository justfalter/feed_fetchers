import requests
import re
from pymemcache.client import Client

# User defined variables
feedaddr = 'https://www.dan.me.uk/torlist/'
feedID = 'dan_me_uk_torlist'
mkey = 'fetcher_dan_me_uk_torlistIP:feeddata'
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
	if len(x) == 0: continue
	print("%s,%s,%s,%s" % (x, feedID, killchain, 'Tor exit node'))
	
