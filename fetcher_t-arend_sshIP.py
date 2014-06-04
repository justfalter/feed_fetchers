import requests
import re
from pymemcache.client import Client

feedaddr = 'http://www.t-arend.de/linux/badguys.txt'
feedID = 't-arend_ssh'
mkey = 'fetcher_t-arend_sshIP:feeddata'
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

for x in splitlines:
	x = x.strip()
	if re.search('^#', x): continue
	xlist = x.split()
	if len(xlist[0]) == 0: continue
	print("%s,%s,%s,%s" % (xlist[1], feedID, killchain, 'SSH scanning'))
	
