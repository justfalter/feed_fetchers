import re
import shutil
import requests
import gzip
import os
import json

# Set the URL path
url = 'http://data.phishtank.com/data/xxxxxxxx/online-valid.json.gz'
filename = 'verified_online.json.gz'
feedID = 'phishtank'
killchain = 'Exploit'

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
json_ar = json.loads(file_content)
del file_content

print('domain,feedID,killchain,description,target,phish_id,url,phish_detail_url')

for item in json_ar:
	domain = item['url']
	domain = re.sub('^.*\:\/\/', '', domain)
	domain = re.sub('\/.*$', '', domain)
	print("%s,%s,%s,%s,%s,%s,%s,%s" % (domain, feedID, killchain, 'Phishtank malicious domain', item['target'], item['phish_id'], item['url'], item['phish_detail_url']))

os.remove(filename)
