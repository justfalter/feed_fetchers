import requests
import re
from pymemcache.client import Client
from datetime import date
from xml.dom.minidom import parseString
import sys

# User defined variables
feedaddr = 'https://isc.sans.edu/api/topips/records/1000/'
feedID = 'dshieldtopsources'
mkey = 'fetcher_dshieldTopsources:feeddata'
killchain = 'Reconnaissance'

# No user modifications needed below.
client = Client(('localhost', 11211))
result = client.get(mkey)

# Generate the date-formatted string for the request
d = date.today()
t = d.timetuple()
today = d.isoformat()
feedaddr+=today # concat the base URL with the date for the full URL

if isinstance(result, str):
	dom = parseString(result)
else:
	r = requests.get(feedaddr)
	client.set(mkey, r.content, expire=7200)
	dom = parseString(r.content)

xmlroot = dom.getElementsByTagName("topips")[0] # Select the root node
print('ipv4,feedID,killchain,description,rank,reports,targets')

for ipaddress in xmlroot.getElementsByTagName("ipaddress"):
	ip = re.sub('^0*', '', ipaddress.getElementsByTagName('source')[0].firstChild.nodeValue) # Strip leading zero(s)
	ip = re.sub('\.[0*]', '.', ip) # Strip subsequent octet-leading zeros
	sys.stdout.write(ip)
	sys.stdout.write(',')
	sys.stdout.write(feedID)
	sys.stdout.write(',')
	sys.stdout.write(killchain)
	sys.stdout.write(',')
	sys.stdout.write('Top malicious sources,')
	sys.stdout.write(ipaddress.getElementsByTagName('rank')[0].firstChild.nodeValue)
	sys.stdout.write(',')
	sys.stdout.write(ipaddress.getElementsByTagName('reports')[0].firstChild.nodeValue)
	sys.stdout.write(',')
	sys.stdout.write(ipaddress.getElementsByTagName('targets')[0].firstChild.nodeValue)
	print # End the line with a \n

