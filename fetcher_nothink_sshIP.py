import requests
import re
from pymemcache.client import Client

feedaddr = 'http://www.nothink.org/blacklist/blacklist_ssh_day.txt'
feedID = 'nothink_sshIP'
mkey = 'fetcher_nothink_sshIP:feeddata'
killchain = 'Reconnaissance'

client = Client(('localhost', 11211))
result = client.get(mkey)

if isinstance(result, str):
	splitlines = result.split('\n')
else:
	r = requests.get(feedaddr)
	client.set(mkey, r.content, expire=7200)
	splitlines = r.content.split('\n')

print('ipv4,feedID,killchain,description')

seen = []

for x in splitlines:
	x = x.strip()
	if re.search('^#', x): continue
	if len(x) == 0: continue
	if x in seen: continue
	seen.append(x)
	print("%s,%s,%s,%s" % (x, feedID, killchain, 'SSH abusers'))
	
