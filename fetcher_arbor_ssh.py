import requests
import re
from pymemcache.client import Client

feedaddr = 'http://atlas-public.ec2.arbor.net/public/ssh_attackers'
feedID = 'arbor_sshattackers'
mkey = 'fetcher_arbor_sshattackerIP:feeddata'
killchain = 'Reconnaissance'

client = Client(('localhost', 11211))
result = client.get(mkey)

if isinstance(result, str):
	splitlines = result.split('\n')
else:
	r = requests.get(feedaddr)
	client.set(mkey, r.content, expire=7200)
	splitlines = r.content.split('\n')
	splitlines.pop(-1)

print('ipv4,feedID,killchain,description,attacks')

for x in splitlines:
	x = x.strip()
	if re.search('^#', x): continue
	xlist = x.split()
	if len(xlist[0]) == 0: continue
	print("%s,%s,%s,%s,%s" % (xlist[0], feedID, killchain, 'SSH Dictionary attacker', xlist[1]))
	
