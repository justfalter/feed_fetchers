import requests
import re

# User defined variables
feedaddr = 'https://raw.githubusercontent.com/EmergingThreats/et-open-bad-ip-list/master/IPs.txt'
feedID = 'et_open_bad_ip_list'
killchain = 'Command & Control'

r = requests.get(feedaddr)
splitlines = r.content.split('\n')

print('ipv4,feedID,killchain,description,firstseen')

for x in splitlines:
	x = x.strip()
	if re.search('^#', x): continue
	if len(x) == 0: continue
	xsplit = x.split('; ')
	xsplit[1] = re.sub('\/.*$', '', xsplit[1])
	print("%s,%s,%s,%s,%s" % (xsplit[1], feedID, killchain, xsplit[2], xsplit[0]))
	
