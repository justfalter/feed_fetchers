# Note: the path we are looking for isn't valid every day
# the file is regen once a week. We drop out if it doesn't exist.

import re
import shutil
import requests
import gzip
import os
from datetime import date

# Set the URL path
d = date.today()
ts = d.strftime("%Y%m%d")
url = 'http://openntpproject.org/parsed-data/parsed2.'
url += ts
url += '.out.gz'

filename = 'parsed2.openntp.out.gz'
feedID = 'openntp_parsed'
killchain = 'unknown'

# Check and see if the remote path exists or not
r = requests.head(url)
if r.status_code != requests.codes.ok:
	exit()
del r

# Fetch the file
os.remove(filename)
response = requests.get(url)
with open(filename, 'wb') as out_file:
    shutil.copyfileobj(response.raw, out_file)
del response

# Read the contents
f = gzip.open(filename, 'rb')
file_content = f.read()
f.close()
splitlines = file_content.split('\n')
del file_content

print('ipv4,feedID,killchain,description')

for x in splitlines:
	x = x.strip()
	if len(x) == 0: continue
	xlist = x.split(':')
	print("%s,%s,%s,%s" % (xlist[0], feedID, killchain, 'OpenNTP IP'))
	
os.remove(filename)
