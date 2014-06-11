import requests
import re
import time

# User defined variables
feedaddr = 'http://stefan.gofferje.net/sipblocklist.zone'
feedID = 'gofferje_SIP'
killchain = 'Reconnaissance'

r = requests.get(feedaddr)
splitlines = r.content.split('\n')

print('ipv4prefix,feedID,killchain,description')

for x in splitlines:
	x = x.strip()
	if not re.search('^\d', x): continue
	if len(x) == 0: continue
	print("%s,%s,%s,%s" % (x, feedID, killchain, 'SIP abuse IP prefix'))
	
