import requests
import re
from pymemcache.client import Client

feedaddr = 'https://palevotracker.abuse.ch/blocklists.php?download=domainblocklist'
feedID = 'palevotracker'
mkey = 'fetcher_palevoDomain:feeddata'
killchain = 'Command & Control'

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
	if re.search('^#', x): continue
	if len(x) == 0: continue
	print("%s,%s,%s,%s" % (x, feedID, killchain, 'Palevo C&C'))
	
