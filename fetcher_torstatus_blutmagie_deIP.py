import requests
import re
from pymemcache.client import Client

# User defined variables
feedaddr = 'http://torstatus.blutmagie.de/ip_list_exit.php/Tor_ip_list_EXIT.csv'
feedID = 'torstatus_blutmagie'
mkey = 'fetcher_torstatus_blutmagie_de:feeddata'
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
	if len(x) == 0: continue
	if x in seen: continue
	seen.append(x)
	print("%s,%s,%s,%s" % (x, feedID, killchain, 'Tor exit node'))
	
