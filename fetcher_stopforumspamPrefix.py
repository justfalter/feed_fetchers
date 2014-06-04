import requests
import re
from pymemcache.client import Client

feedaddr = 'http://www.stopforumspam.com/downloads/toxic_ip_cidr.txt'
feedID = 'stopforumspam'
mkey = 'fetcher_stopforumspamPrefix:feeddata'
killchain = 'unknown'

client = Client(('localhost', 11211))
result = client.get(mkey)

if isinstance(result, str):
	splitlines = result.split('\n')
else:
	r = requests.get(feedaddr)
	client.set(mkey, r.content, expire=7200)
	splitlines = r.content.split('\n')

seen = []

print('ipv4prefix,feedID,killchain,description')

for x in splitlines:
	x = x.strip()
	if not re.search('^\d', x): continue
	if len(x) == 0: continue
	if x in seen: continue
	seen.append(x)
	print("%s,%s,%s,%s" % (x, feedID, killchain,'Malicious prefix'))
	
