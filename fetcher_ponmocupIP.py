import requests
import re
from pymemcache.client import Client

# User defined variables
feedaddr = 'http://security-research.dyndns.org/pub/botnet/ponmocup/ponmocup-finder/ponmocup-infected-domains-latest.txt'
feedID = 'ponmocup'
mkey = 'fetcher_ponmocupDomain:feeddata'
killchain = 'Delivery'

# No user modifications needed below.
client = Client(('localhost', 11211))
result = client.get(mkey)

if isinstance(result, str):
	splitlines = result.split('\n')
else:
	r = requests.get(feedaddr)
	client.set(mkey, r.content, expire=7200)
	splitlines = r.content.split('\n')

print('ipv4,feedID,killchain,description,url,domain')

for x in splitlines:
	x = x.strip()
	if re.search('^#', x): continue
	if re.search('^date started', x): continue
	if re.search('^date finished', x): continue
	if len(x) == 0: continue
	ip = re.sub('^.* ', '', x)
	if not re.search('^[0-9]', ip): continue
	xsplit = x.split()
	print("%s,%s,%s,%s,%s,%s" % (ip, feedID, killchain, 'Ponmocup delivery domain', xsplit[8], xsplit[2]))
	
