import requests
import re
from pymemcache.client import Client

# User defined variables
feedaddr = 'http://vxvault.siri-urz.net/URL_List.php'
feedID = 'vxvault'
mkey = 'fetcher_vxvault:feeddata'
killchain = 'Exploit'

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
	
print('domain,feedID,killchain,description')

for x in splitlines:
	x = x.strip()
	if not x.startswith("htt"): continue
	x = re.sub('http\:\/\/', '', x)
	x = re.sub('\/.*$', '', x)
	if re.search('[a-z,A-Z]', x):
		if x in seen: continue
		seen.append(x)
		print("%s,%s,%s,%s" % (x, feedID, killchain, 'Malware hosting domain'))
	
