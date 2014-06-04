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
feedID = 'threatconnect_subscriber_community'
community = 'Common%20Community'
limit = '500'

accessID = 'accessID'
secret_key = 'secretkey'
request = '/v1/indicators?owner='+community+'&resultStart=0&resultLimit=500'
headers = generate_headers('GET', request, accessID, secret_key)
resp = requests.get('https://api.threatconnect.com'+request, headers=headers)
reports = json.loads(resp.content)

ilist = reports['data']['indicator']
print('ipv4,feedID,description,webLink,dateAdded')

for x in ilist:
	if re.search('[a-z,A-Z]', x['summary']): continue
	print("%s,%s,%s,%s,%s" % (x['summary'], feedID, 'ThreatConnect observed IP', x['webLink'], x['dateAdded']))
	
	
