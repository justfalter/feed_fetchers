import requests
import re
import time

# User defined variables
feedaddr = 'https://security.berkeley.edu/aggressive_ips/ips'
feedID = 'berkeley_security_aggressive'
killchain = 'Reconnaissance'

r = requests.get(feedaddr)
splitlines = r.content.split('\n')

print('ipv4,feedID,killchain,description,lastseen')

for x in splitlines:
	x = x.strip()
	if not re.search('^HOSTILE', x): continue
	if len(x) == 0: continue
	xsplit = x.split()
	lastseen = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(xsplit[3])))
	print("%s,%s,%s,%s,%s" % (xsplit[1], feedID, killchain, 'Berkeley Security Aggressive IP', lastseen))
	
