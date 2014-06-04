import requests
import re
from datetime import date, timedelta
import os
import shutil
import gzip

feedID = 'cleanmx_phishwatch'
killchain = 'Exploit'

feedaddr = 'http://lists.clean-mx.com/pipermail/phishwatch/'
yesterday = date.today() - timedelta(1)
urldate = yesterday.isoformat()
urldate = re.sub('\-', '', urldate)
feedaddr+=urldate # concat the base URL with the date for the full URL
feedaddr+='.txt.gz'

filename = urldate + '.txt.gz'

# Fetch the file
if os.path.isfile(filename): os.remove(filename)
response = requests.get(feedaddr)
with open(filename, 'wb') as out_file:
    shutil.copyfileobj(response.raw, out_file)
del response

# Read the contents
f = gzip.open(filename, 'rb')
file_content = f.read()
f.close()
splitlines = file_content.split('\n')
del file_content

print('ipv4,feedID,killchain,description,url')

for x in splitlines:
	x = x.strip()
	if len(x) == 0: continue
	if re.search('^Up\(nil', x):
		xsplit = x.split()
		print("%s,%s,%s,%s,%s" % (xsplit[1], feedID, killchain, 'CleanMX Phishing IPs',xsplit[5]))

