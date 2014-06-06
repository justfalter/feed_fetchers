import requests
import re
import time, base64,hmac, hashlib
import json

def generate_headers(verb, path, accessID, secret_key):
    """
    Create the ThreatConnect authentication headers.
    """
    timestamp = str(int(time.time()))
    signature = "%s:%s:%s" % (path, verb, timestamp)
    hmac_signature = hmac.new(secret_key, signature, digestmod=hashlib.sha256).digest()
    authorization = 'TC %s:%s' % (accessID, base64.b64encode(hmac_signature))
    headers = {'timestamp': timestamp, 'authorization': authorization}
    return headers
	
# User defined variables
feedID = 'threatconnect_Common_community'
community = 'Common%20Community'
killchain = 'unknown'

accessID = '0000000000000000'
secret_key = 'xxxxxxxxxxxxxxxxx'

total_count = 0
todo_count = 500 # Initially setting it to anything above 0
toprint = []

while total_count < todo_count:
	request = '/v1/indicators?owner='+community+'&resultStart='+str(total_count)+'&resultLimit=500'
	headers = generate_headers('GET', request, accessID, secret_key)
	resp = requests.get('https://api.threatconnect.com'+request, headers=headers)
	reports = json.loads(resp.content)
	try:
		todo_count = reports['data']['resultCount']
		# Only shows up in the first request, nothing after offset
	except:
		pass
	ilist = reports['data']['indicator']
	for x in ilist:
		total_count += 1
		if x['type'] == 'URL':
			tmp_list = {}
			tmp_list['url'] = x['summary']
			tmp_list['webLink'] = x['webLink']
			tmp_list['dateAdded'] = x['dateAdded']
			toprint.append(tmp_list)
			del tmp_list
	
print('url,feedID,killchain,description,webLink,dateAdded')
for x in toprint:
	print("%s,%s,%s,%s,%s,%s" % (x['url'], feedID, killchain,'ThreatConnect observed URL', x['webLink'], x['dateAdded']))

