import requests
import re
from datetime import date, timedelta

feedaddr = 'http://1d4.us/archive/domain-'
yesterday = date.today() - timedelta(1)
ts = yesterday.strftime("%d-%m-%Y")
feedaddr += ts
feedaddr += '.txt'

feedID = '1d4_domain'
killchain = 'unknown'

r = requests.get(feedaddr)
splitlines = r.content.split('\n')

print('domain,feedID,killchain,description,context_hits')

if r.status_code != 200: exit()
for x in splitlines:
	x = x.strip()
	if re.search('^#', x): continue
	if len(x) == 0: continue
	xsplit = x.split()
	if not xsplit[1] == '.':
		xsplit[1] = re.sub('\.$', '', xsplit[1])
		print("%s,%s,%s,%s,%s" % (xsplit[1], feedID, killchain, 'Unknown context hit', xsplit[0]))
	
