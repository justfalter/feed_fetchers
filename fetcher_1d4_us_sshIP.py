import requests
import re
from datetime import date, timedelta

feedaddr = 'http://1d4.us/archive/ssh-'
yesterday = date.today() - timedelta(1)
ts = yesterday.strftime("%d-%m-%Y")
feedaddr += ts
feedaddr += '.txt.txt'

feedID = '1d4_ssh'
killchain = 'unknown'

r = requests.get(feedaddr)
splitlines = r.content.split('\n')

print('ipv4,feedID,killchain,description')

if r.status_code != 200: exit()
for x in splitlines:
	x = x.strip()
	if re.search('^#', x): continue
	if len(x) == 0: continue
	print("%s,%s,%s,%s" % (x, feedID, killchain, 'Unknown SSH context hit'))
	
