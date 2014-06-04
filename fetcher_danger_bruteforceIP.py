import requests
import re
from pymemcache.client import Client

# User defined variables
feedaddr = 'http://danger.rulez.sk/projects/bruteforceblocker/blist.php'
feedID = 'dangerbruteforce'
mkey = 'fetcher_danger_bruteforceIP:feeddata'
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

print('ipv4,feedID,killchain,description,date,count,id')

for x in splitlines:
	x = x.strip()
	if re.search('^#', x): continue
	if len(x) == 0: continue
	xlist = x.split() # Break up the line by whitespace
	print("%s,%s,%s,%s %s,%s,%s,%s" % (xlist[0], feedID, killchain, 'Bruteforce scanner', xlist[2], xlist[3], xlist[4], xlist[5]))
	
