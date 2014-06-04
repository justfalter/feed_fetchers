import requests
import re
import json

# User defined variables
feedaddr = 'https://api.github.com/users/jedisct1/gists'
feedID = 'gist_jedisct1'
killchain = 'Delivery'

r = requests.get(feedaddr)
json_ar = json.loads(r.content)

urllist = []

for file in json_ar:
	for filename in  file['files']:
		name = str(filename)
		urllist.append(file['files'][name]['raw_url'])

domlist = []
		
for url in urllist:
	urlrequest = requests.get(url)
	splitlines = urlrequest.content.split('\n')
	for line in splitlines:
		if re.search('[a-z,0-9]\.[a-z]', line):
			xlist = line.split()
			xlist[0] = re.sub('\.$', '', xlist[0])
			if re.search('[a-z,0-9]\.[a-z]', xlist[0]) and not re.search('[\{,\},\:]', xlist[0]):
				domlist.append(xlist[0])
		
print('domain,feedID,killchain,description')

for x in domlist:
	if len(x) == 0: continue
	print("%s,%s,%s,%s" % (x, feedID, killchain, 'Possible malicious domain'))
	
