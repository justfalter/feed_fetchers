import urllib, zipfile, cStringIO, os
import re

# User defined variables
feedaddr = 'http://s3.amazonaws.com/alexa-static/top-1m.csv.zip'
zipfilename = 'top-1m.csv'
feedID = 'alexatop1m'
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

print('domain,feedID,killchain,description,rank')

for x in splitlines:
	x = x.strip()
	x = re.sub('"', '', x)
	if len(x) == 0: continue
	xlist = x.split(',') # Break up the line by comma
	print("%s,%s,%s,%s,%s" % (xlist[1], feedID, killchain, 'Alexa Top Domains',xlist[0]))
	
