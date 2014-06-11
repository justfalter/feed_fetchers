import requests
import re
import time

# User defined variables
feedaddr = 'http://www.cruzit.com/xwbl2txt.php'
feedID = 'cruzit_blacklist'
killchain = 'Reconnaissance'

r = requests.get(feedaddr)
splitlines = r.content.split('\n')

print('ipv4,feedID,killchain,description')

for x in splitlines:
	x = x.strip()
	if not re.search('^\d', x): continue
	if len(x) == 0: continue
	print("%s,%s,%s,%s" % (x, feedID, killchain, 'Cruzit Blacklist IP'))
	
