import urllib, zipfile, cStringIO, os, json
import re
from pymemcache.client import Client

feedaddr = 'http://www.stopforumspam.com/downloads/listed_ip_1_all.zip'
zipfilename = 'listed_ip_1_all.txt'
feedID = 'stopforumspam'
mkey = 'fetcher_stopforumspamIP:feeddata'
killchain = 'unknown'

client = Client(('localhost', 11211))
result = client.get(mkey)

if isinstance(result, str):
	splitlines = result.split('\n')
else:
	if os.path.isfile(zipfilename): os.remove(zipfilename)
	zipwebfile = urllib.urlopen(feedaddr)
	buffer = cStringIO.StringIO(zipwebfile.read())
	zfile = zipfile.ZipFile(buffer)
	myfile = zfile.extract('listed_ip_1_all.txt')
	f = open(zipfilename, 'r')
	splitlines = f.read()
	client.set(mkey, splitlines, expire=7200)
	splitlines = splitlines.split('\n')
	if os.path.isfile(zipfilename): os.remove(zipfilename)

seen = []

print('ipv4,feedID,killchain,description')

for x in splitlines:
	x = x.strip()
	x = re.sub('"', '', x)
	x = re.sub(',.*$', '', x)
	if not re.search('^\d', x): continue
	if len(x) == 0: continue
	if x in seen: continue
	seen.append(x)
	print("%s,%s,%s,%s" % (x, feedID, killchain, 'Malicious IP'))
	
