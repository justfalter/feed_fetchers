import requests
import re
from pymemcache.client import Client

# User defined variables
feedaddr = 'http://feeds.dshield.org/block.txt'
feedID = 'dshieldtop20'
mkey = 'fetcher_dshieldPrefix:feeddata'
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

print('ipv4prefix,feedID,killchain,description')

for x in splitlines:
	x = x.strip()
	if not re.search('^\d', x): continue
	if len(x) == 0: continue
	# So now we have a line like
	# 60.172.228.0	60.172.228.255	24	6511	CHINANET-BACKBONE No.31,Jin-rong Street	CN	wang@mail.hf.ah.cninfo.net
	# This is supposed to only be /24's
	x = re.sub('\t.*$', '', x)
	print("%s/24,%s,%s,%s" % (x, feedID, killchain, 'dShield Top 20 malicious prefix'))
	
