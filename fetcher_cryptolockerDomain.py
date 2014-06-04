import requests
import re
from pymemcache.client import Client

# User defined variables
feedaddr = 'http://osint.bambenekconsulting.com/feeds/cl-domlist.txt'
feedID = 'cryptolocker'
mkey = 'fetcher_cryptolockerDomain:feeddata'
killchain = 'Command & Control'

# No user modifications needed below.
client = Client(('localhost', 11211))
result = client.get(mkey)

if isinstance(result, str):
	splitlines = result.split('\n')
else:
	r = requests.get(feedaddr)
	client.set(mkey, r.content, expire=7200)
	splitlines = r.content.split('\n')

print('domain,feedID,killchain,description,date')

for x in splitlines:
	x = x.strip()
	if re.search('^#', x): continue
	if len(x) == 0: continue
	xlist = x.split(',') # Break up the line by comma
	print("%s,%s,%s,%s,%s" % (xlist[0], feedID, killchain, xlist[1], xlist[2]))
	
