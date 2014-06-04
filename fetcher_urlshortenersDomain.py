import urllib, zipfile, cStringIO, os
import re

# User defined variables
feedaddr = 'http://mirror3.malwaredomains.com/files/url_shorteners.zip'
zipfilename = 'url_shorteners.txt'
feedID = 'url_shorteners'
mkey = 'fetcher_url_shortenersDomain:feeddata'
killchain = 'unknown'

if os.path.isfile(zipfilename): os.remove(zipfilename)
zipwebfile = urllib.urlopen(feedaddr)
buffer = cStringIO.StringIO(zipwebfile.read())
zfile = zipfile.ZipFile(buffer)
myfile = zfile.extract(zipfilename)

# Now it's extracted to the local directory
f = open(zipfilename, 'r')
splitlines = f.read()
splitlines = splitlines.split('\n')
if os.path.isfile(zipfilename): os.remove(zipfilename)

print('domain,feedID,killchain,description,url')

for x in splitlines:
	x = x.strip()
	if re.search('^#', x): continue
	if len(x) == 0: continue
	x = re.sub('\*\.', '', x)
	x = re.sub('\* ', '', x)
	x = re.sub('\/#', '\t#', x)
	if re.search('\t#', x):
		xlist = x.split('\t#') # Break up the line
		print("%s,%s,%s,%s,%s" % (xlist[0], feedID, killchain, 'URL Shorteners',xlist[1]))
	else:
		print("%s,%s,%s,%s," % (x, feedID, killchain, 'URL Shorteners'))
	
